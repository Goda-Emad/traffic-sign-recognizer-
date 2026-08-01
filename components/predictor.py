import numpy as np
import streamlit as st
import tensorflow as tf
from core.constants import MODEL_PATH, CLASS_LABELS
from utils.image_utils import preprocess_image


@st.cache_resource
def load_model():
    """Load Keras model once and cache it."""
    return tf.keras.models.load_model(MODEL_PATH, compile=False)


def predict(image):
    """
    Run inference on a PIL image.
    Returns: (preds, top_idx, (emoji, label))
    """
    model = load_model()
    img_array = preprocess_image(image)
    preds = model.predict(img_array, verbose=0)[0]
    top_idx = int(np.argmax(preds))
    emoji, label = CLASS_LABELS[top_idx]
    return preds, top_idx, (emoji, label)
