import streamlit as st
from components.sidebar import render_sidebar, get_text
from components.ui import render_header, load_css
from core.constants import CLASS_LABELS

st.set_page_config(
    page_title="Home 🏠",
    page_icon="🚦",
    layout="wide"
)

load_css()
render_sidebar()

# ── Hero Section ─────────────────────────────────────
st.markdown(f"""
<div style='text-align:center; padding: 3rem 0 2rem 0;'>
    <h1 style='font-size:3rem; font-weight:800; color:#E63946;'>
        🚦 {get_text("Traffic Sign Recognizer", "نظام التعرف على إشارات المرور")}
    </h1>
    <p style='font-size:1.2rem; color:#888; max-width:600px; margin:auto;'>
        {get_text(
            "AI-powered web app that classifies traffic signs instantly using Deep Learning.",
            "تطبيق ذكاء اصطناعي يصنف إشارات المرور فورياً باستخدام التعلم العميق."
        )}
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ── Stats ─────────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(get_text("Model", "الموديل"), "MobileNet")
with col2:
    st.metric(get_text("Classes", "التصنيفات"), "5")
with col3:
    st.metric(get_text("Training Images", "صور التدريب"), "6,390+")
with col4:
    st.metric(get_text("Accuracy", "الدقة"), "100%")

st.divider()

# ── How It Works ──────────────────────────────────────
st.markdown(f"### {get_text('⚙️ How It Works', '⚙️ كيف يعمل؟')}")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class='result-card' style='text-align:center; padding:1.5rem;'>
        <div style='font-size:2.5rem;'>📤</div>
        <h3 style='color:#E63946;'>01</h3>
        <p>{get_text("Upload a traffic sign image", "ارفع صورة إشارة المرور")}</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class='result-card' style='text-align:center; padding:1.5rem;'>
        <div style='font-size:2.5rem;'>🧠</div>
        <h3 style='color:#E63946;'>02</h3>
        <p>{get_text("AI analyzes the image instantly", "الذكاء الاصطناعي يحلل الصورة فوراً")}</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class='result-card' style='text-align:center; padding:1.5rem;'>
        <div style='font-size:2.5rem;'>✅</div>
        <h3 style='color:#E63946;'>03</h3>
        <p>{get_text("Get prediction with confidence score", "احصل على النتيجة مع نسبة الثقة")}</p>
    </div>
    """, unsafe_allow_html=True)
