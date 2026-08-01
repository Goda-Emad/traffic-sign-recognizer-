import streamlit as st


def save_prediction(image_name: str, label: str, emoji: str, confidence: float):
    """Save a prediction to session state history."""
    if "history" not in st.session_state:
        st.session_state["history"] = []

    st.session_state["history"].append({
        "image":      image_name,
        "label":      label,
        "emoji":      emoji,
        "confidence": round(confidence * 100, 2)
    })


def get_history() -> list:
    """Return prediction history from session state."""
    return st.session_state.get("history", [])


def clear_history():
    """Clear all prediction history."""
    st.session_state["history"] = []
