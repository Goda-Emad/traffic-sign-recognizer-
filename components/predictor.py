import os
os.environ["TF_USE_LEGACY_KERAS"] = "1"

import json
import tempfile
import shutil

import h5py
import numpy as np
import streamlit as st
import tensorflow as tf

from core.constants import MODEL_PATH, CLASS_LABELS
from utils.image_utils import preprocess_image


# ── Patch ─────────────────────────────────────────────────────────────────────

def _patch_h5_model(src_path: str, dst_path: str) -> None:
    """
    Copy the .h5 model to dst_path, removing the unsupported
    'groups' key from every DepthwiseConv2D layer config
    (Keras-2 → Keras-3 compatibility fix).
    """
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


# ── Model loader ──────────────────────────────────────────────────────────────

@st.cache_resource(show_spinner="Loading model…")
def load_model() -> tf.keras.Model:
    """
    Load the Keras .h5 model with DepthwiseConv2D patch applied.
    Cached across sessions — only runs once per server boot.
    """
    patched_path = os.path.join(
        tempfile.gettempdir(), "traffic_sign_model_patched.h5"
    )

    try:
        if not os.path.exists(patched_path):
            _patch_h5_model(MODEL_PATH, patched_path)

        model = tf.keras.models.load_model(patched_path, compile=False)
        return model

    except FileNotFoundError:
        st.error("❌ Model file not found. Make sure `model/keras_model.h5` exists.")
        st.stop()

    except Exception as e:
        st.error(f"❌ Failed to load model: {e}")
        st.stop()


# ── Inference ─────────────────────────────────────────────────────────────────

def predict(image) -> tuple[np.ndarray, int, tuple[str, str]]:
    """
    Run inference on a PIL image.

    Args:
        image: PIL.Image — raw image uploaded by the user.

    Returns:
        preds     (np.ndarray)    — softmax confidence scores for all classes.
        top_idx   (int)           — index of the highest-confidence class.
        (emoji, label) (tuple)    — human-readable label from CLASS_LABELS.

    Raises:
        KeyError: if top_idx is not found in CLASS_LABELS.
    """
    model     = load_model()
    img_array = preprocess_image(image)
    preds     = model.predict(img_array, verbose=0)[0]
    top_idx   = int(np.argmax(preds))

    if top_idx not in CLASS_LABELS:
        st.error(f"❌ Unexpected class index: {top_idx}")
        st.stop()

    emoji, label = CLASS_LABELS[top_idx]
    return preds, top_idx, (emoji, label)
