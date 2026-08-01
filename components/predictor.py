import os
os.environ["TF_USE_LEGACY_KERAS"] = "1"

import json
import numpy as np
import streamlit as st
import tensorflow as tf
import h5py

from core.constants import MODEL_PATH, CLASS_LABELS
from utils.image_utils import preprocess_image


def _patch_h5_model(src_path: str, dst_path: str) -> None:
    """
    Copy the .h5 model to dst_path, removing the unsupported
    'groups' key from every DepthwiseConv2D layer config.
    """
    import shutil
    shutil.copy2(src_path, dst_path)

    with h5py.File(dst_path, "r+") as f:
        if "model_config" not in f.attrs:
            return

        raw = f.attrs["model_config"]
        if isinstance(raw, bytes):
            raw = raw.decode("utf-8")

        cfg = json.loads(raw)

        def _fix(node):
            if isinstance(node, dict):
                if node.get("class_name") == "DepthwiseConv2D":
                    node.get("config", {}).pop("groups", None)
                for v in node.values():
                    _fix(v)
            elif isinstance(node, list):
                for item in node:
                    _fix(item)

        _fix(cfg)
        f.attrs["model_config"] = json.dumps(cfg)


@st.cache_resource(show_spinner="Loading model...")
def load_model() -> tf.keras.Model:
    """
    Load the Keras .h5 model, patching Keras-2 → Keras-3
    incompatibility (DepthwiseConv2D 'groups' argument).
    Falls back gracefully with a clear error message.
    """
    import tempfile

    patched_path = os.path.join(
        tempfile.gettempdir(), "traffic_sign_model_patched.h5"
    )

    try:
        if not os.path.exists(patched_path):
            _patch_h5_model(MODEL_PATH, patched_path)

        model = tf.keras.models.load_model(patched_path, compile=False)
        return model

    except Exception as e:
        st.error(f"❌ Failed to load model: {e}")
        st.stop()


def predict(image):
    """
    Run inference on a PIL image.

    Args:
        image: PIL.Image — raw image from the user.

    Returns:
        preds    (np.ndarray) — confidence scores for all classes.
        top_idx  (int)        — index of the top prediction.
        (emoji, label)        — human-readable label tuple.
    """
    model     = load_model()
    img_array = preprocess_image(image)
    preds     = model.predict(img_array, verbose=0)[0]
    top_idx   = int(np.argmax(preds))
    emoji, label = CLASS_LABELS[top_idx]

    return preds, top_idx, (emoji, label)
