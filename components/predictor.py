import os
import numpy as np
import streamlit as st

# ── Force TF to use its own bundled Keras 2 (tf.keras) ───────────
# Must be set BEFORE any keras/tensorflow import
os.environ["TF_USE_LEGACY_KERAS"] = "1"

import tensorflow as tf
from core.constants import MODEL_PATH, CLASS_LABELS
from utils.image_utils import preprocess_image


@st.cache_resource
def load_model():
    """Load Keras .h5 model with Keras-2-compatible loader."""
    try:
        # ── Approach 1: tf.keras (Keras 2 bundled inside TF) ─────
        model = tf.keras.models.load_model(MODEL_PATH, compile=False)
        return model

    except TypeError:
        # ── Approach 2: patch DepthwiseConv2D to drop 'groups' ───
        # Keras 3 added 'groups' to DepthwiseConv2D config but the
        # old .h5 files include it, causing a TypeError on load.
        from tensorflow.keras.layers import DepthwiseConv2D as _DW

        class _PatchedDepthwiseConv2D(_DW):
            def __init__(self, **kwargs):
                kwargs.pop("groups", None)   # remove unsupported arg
                super().__init__(**kwargs)

            @classmethod
            def from_config(cls, config):
                config.pop("groups", None)
                return super().from_config(config)

        custom_objects = {"DepthwiseConv2D": _PatchedDepthwiseConv2D}

        model = tf.keras.models.load_model(
            MODEL_PATH,
            custom_objects=custom_objects,
            compile=False,
        )
        return model


def predict(image):
    """
    Run inference on a PIL image.
    Returns: (preds, top_idx, (emoji, label))
    """
    model     = load_model()
    img_array = preprocess_image(image)
    preds     = model.predict(img_array, verbose=0)[0]
    top_idx   = int(np.argmax(preds))
    emoji, label = CLASS_LABELS[top_idx]
    return preds, top_idx, (emoji, label)
