import streamlit as st
from core.config import APP_NAME, APP_ICON, APP_VERSION
from components.sidebar import render_sidebar, get_text
from components.ui import render_header, load_css

st.set_page_config(
    page_title=APP_NAME,
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()
render_sidebar()

# ── Hero Section ─────────────────────────────────────
st.markdown(f"""
<div style='text-align:center; padding: 3rem 0 2rem 0;'>
    <h1 style='font-size:3.5rem; font-weight:800; color:#E63946;'>
        🚦 {get_text("Traffic Sign Recognizer", "نظام التعرف على إشارات المرور")}
    </h1>
    <p style='font-size:1.2rem; color:#888; max-width:600px; margin:auto;'>
        {get_text(
            "AI-powered web app that classifies traffic signs instantly using Deep Learning.",
            "تطبيق ذكاء اصطناعي يصنف إشارات المرور فورياً باستخدام التعلم العميق."
        )}
    </p>
    <p style='color:#555; font-size:0.85rem; margin-top:1rem;'>v{APP_VERSION}</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ── Navigation Cards ──────────────────────────────────
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class='result-card' style='text-align:center; padding:2rem 1rem; cursor:pointer;'>
        <div style='font-size:2.5rem;'>🏠</div>
        <h3 style='color:#E63946;'>{get_text("Home", "الرئيسية")}</h3>
        <p style='color:#888; font-size:0.85rem;'>{get_text("Project intro & overview", "مقدمة ونظرة عامة")}</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button(get_text("Go →", "اذهب →"), key="home", use_container_width=True):
        st.switch_page("pages/1_🏠_Home.py")

with col2:
    st.markdown(f"""
    <div class='result-card' style='text-align:center; padding:2rem 1rem; cursor:pointer;'>
        <div style='font-size:2.5rem;'>🔍</div>
        <h3 style='color:#E63946;'>{get_text("Predict", "تنبؤ")}</h3>
        <p style='color:#888; font-size:0.85rem;'>{get_text("Upload & classify signs", "ارفع وصنف الإشارات")}</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button(get_text("Go →", "اذهب →"), key="predict", use_container_width=True):
        st.switch_page("pages/2_🔍_Predict.py")

with col3:
    st.markdown(f"""
    <div class='result-card' style='text-align:center; padding:2rem 1rem; cursor:pointer;'>
        <div style='font-size:2.5rem;'>📊</div>
        <h3 style='color:#E63946;'>{get_text("Results", "النتائج")}</h3>
        <p style='color:#888; font-size:0.85rem;'>{get_text("Prediction history & stats", "سجل التنبؤات والإحصائيات")}</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button(get_text("Go →", "اذهب →"), key="results", use_container_width=True):
        st.switch_page("pages/3_📊_Results.py")

with col4:
    st.markdown(f"""
    <div class='result-card' style='text-align:center; padding:2rem 1rem; cursor:pointer;'>
        <div style='font-size:2.5rem;'>ℹ️</div>
        <h3 style='color:#E63946;'>{get_text("About", "عن المشروع")}</h3>
        <p style='color:#888; font-size:0.85rem;'>{get_text("Team & project info", "الفريق ومعلومات المشروع")}</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button(get_text("Go →", "اذهب →"), key="about", use_container_width=True):
        st.switch_page("pages/4_ℹ️_About.py")

st.divider()

st.markdown(
    f"<p style='text-align:center; color:#555;'>v{APP_VERSION} • {get_text('Made with ❤️ by Goda Emad', 'صنع بـ ❤️ بواسطة جودا عماد')}</p>",
    unsafe_allow_html=True
)
