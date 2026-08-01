import streamlit as st
from PIL import Image
from components.sidebar import render_sidebar, get_text
from components.ui import render_header, render_result, load_css
from components.predictor import predict
from components.charts import render_confidence_bar, render_confidence_pie
from core.constants import CLASS_LABELS

st.set_page_config(
    page_title="Predict 🔍",
    page_icon="🔍",
    layout="wide"
)

load_css()
render_sidebar()

# ── Header ────────────────────────────────────────────
render_header(
    get_text("🔍 Predict", "🔍 تنبؤ"),
    get_text(
        "Upload a traffic sign image and get an instant AI prediction.",
        "ارفع صورة إشارة مرور واحصل على تنبؤ فوري."
    )
)

st.divider()

# ── Upload ────────────────────────────────────────────
uploaded_file = st.file_uploader(
    get_text("Upload a traffic sign image", "ارفع صورة إشارة مرور"),
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file)

    col1, col2 = st.columns([1, 1])

    with col1:
        st.image(image, caption=get_text("Uploaded Image", "الصورة المرفوعة"), use_column_width=True)

    with col2:
        with st.spinner(get_text("Analyzing...", "جاري التحليل...")):
            preds, top_idx, (emoji, label) = predict(image)

        render_result(emoji, label, float(preds[top_idx]))

        # Save to history
        if "history" not in st.session_state:
            st.session_state["history"] = []

        st.session_state["history"].append({
            "image": uploaded_file.name,
            "label": label,
            "emoji": emoji,
            "confidence": float(preds[top_idx]) * 100
        })

    st.divider()

    # ── Charts ────────────────────────────────────────
    st.markdown(f"### {get_text('📊 Confidence Analysis', '📊 تحليل الثقة')}")

    col1, col2 = st.columns([1, 1])
    with col1:
        render_confidence_bar(preds)
    with col2:
        render_confidence_pie(preds)

    st.divider()

    # ── All Probabilities ─────────────────────────────
    st.markdown(f"### {get_text('📋 All Probabilities', '📋 كل الاحتمالات')}")

    for idx, conf in sorted(enumerate(preds), key=lambda x: x[1], reverse=True):
        em, lbl = CLASS_LABELS[idx]
        col_a, col_b = st.columns([3, 1])
        with col_a:
            st.progress(float(conf), text=f"{em} {lbl}")
        with col_b:
            st.markdown(f"**{conf*100:.1f}%**")

else:
    # Empty state
    st.markdown(f"""
    <div style='text-align:center; padding:4rem 0; color:#555;'>
        <div style='font-size:4rem;'>📂</div>
        <h3>{get_text("No image uploaded yet", "لم يتم رفع صورة بعد")}</h3>
        <p>{get_text("Upload a traffic sign image above to get started.", "ارفع صورة إشارة مرور للبدء.")}</p>
    </div>
    """, unsafe_allow_html=True)
