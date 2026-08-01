import streamlit as st
import pandas as pd
from components.sidebar import render_sidebar, get_text
from components.ui import render_header, load_css

st.set_page_config(
    page_title="Results 📊",
    page_icon="📊",
    layout="wide"
)

load_css()
render_sidebar()

# ── Header ────────────────────────────────────────────
render_header(
    get_text("📊 Results", "📊 النتائج"),
    get_text(
        "View all your previous predictions in one place.",
        "اعرض كل التنبؤات السابقة في مكان واحد."
    )
)

st.divider()

history = st.session_state.get("history", [])

if not history:
    # ── Empty State ───────────────────────────────────
    st.markdown(f"""
    <div style='text-align:center; padding:4rem 0; color:#555;'>
        <div style='font-size:4rem;'>📭</div>
        <h3>{get_text("No predictions yet", "لا توجد تنبؤات بعد")}</h3>
        <p>{get_text("Go to Predict page and upload an image first.", "اذهب لصفحة التنبؤ وارفع صورة أولاً.")}</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        if st.button(get_text("🔍 Go to Predict", "🔍 اذهب للتنبؤ"), use_container_width=True, type="primary"):
            st.switch_page("pages/2_🔍_Predict.py")

else:
    # ── Stats ─────────────────────────────────────────
    total      = len(history)
    avg_conf   = sum(h["confidence"] for h in history) / total
    top_label  = max(set(h["label"] for h in history), key=lambda x: sum(1 for h in history if h["label"] == x))

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(get_text("Total Predictions", "إجمالي التنبؤات"), total)
    with col2:
        st.metric(get_text("Avg Confidence", "متوسط الثقة"), f"{avg_conf:.1f}%")
    with col3:
        st.metric(get_text("Most Predicted", "الأكثر تنبؤاً"), top_label)

    st.divider()

    # ── History Table ─────────────────────────────────
    st.markdown(f"### {get_text('📋 Prediction History', '📋 سجل التنبؤات')}")

    df = pd.DataFrame(history)
    df.index += 1
    df.columns = [
        get_text("Image", "الصورة"),
        get_text("Label", "التصنيف"),
        get_text("Emoji", "الأيقونة"),
        get_text("Confidence %", "نسبة الثقة %")
    ]

    st.dataframe(df, use_container_width=True)

    st.divider()

    # ── Clear History ─────────────────────────────────
    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        if st.button(get_text("🗑️ Clear History", "🗑️ مسح السجل"), use_container_width=True):
            st.session_state["history"] = []
            st.rerun()
