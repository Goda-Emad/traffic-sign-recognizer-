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

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="home-hero">
    <div class="hero-badge">{get_text("Deep Learning · Computer Vision", "تعلم عميق · رؤية حاسوبية")}</div>
    <h1 class="hero-title">
        🚦 {get_text("Traffic Sign Recognizer", "نظام التعرف على إشارات المرور")}
    </h1>
    <p class="hero-subtitle">
        {get_text(
            "AI-powered web app that classifies traffic signs instantly using Deep Learning.",
            "تطبيق ذكاء اصطناعي يصنف إشارات المرور فورياً باستخدام التعلم العميق."
        )}
    </p>
    <p class="hero-version">v{APP_VERSION}</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ── Stats ─────────────────────────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric(get_text("Model", "الموديل"), "MobileNet")
with c2:
    st.metric(get_text("Classes", "التصنيفات"), "5")
with c3:
    st.metric(get_text("Training Images", "صور التدريب"), "6,390+")
with c4:
    st.metric(get_text("Accuracy", "الدقة"), "95%")

st.divider()

# ── Navigation Cards ──────────────────────────────────────────────────────────
pages = [
    ("🏠", get_text("Home",    "الرئيسية"),   get_text("Project intro & overview",       "مقدمة ونظرة عامة"),           "home",    "pages/1_🏠_Home.py"),
    ("🔍", get_text("Predict", "تنبؤ"),        get_text("Upload & classify signs",        "ارفع وصنف الإشارات"),          "predict", "pages/2_🔍_Predict.py"),
    ("📊", get_text("Results", "النتائج"),     get_text("Prediction history & stats",     "سجل التنبؤات والإحصائيات"),    "results", "pages/3_📊_Results.py"),
    ("ℹ️", get_text("About",   "عن المشروع"), get_text("Team & project info",            "الفريق ومعلومات المشروع"),      "about",   "pages/4_ℹ️_About.py"),
]

cols = st.columns(4)
for col, (icon, title, desc, key, path) in zip(cols, pages):
    with col:
        st.markdown(f"""
        <div class="nav-page-card">
            <div class="nav-page-icon">{icon}</div>
            <div class="nav-page-title">{title}</div>
            <div class="nav-page-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button(get_text("Go →", "اذهب →"), key=key, use_container_width=True):
            st.switch_page(path)

st.divider()

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown(f"""
<p class="about-footer">
    v{APP_VERSION} &nbsp;·&nbsp;
    {get_text("Made with ❤️ by Goda Emad", "صنع بـ ❤️ بواسطة جودا عماد")}
</p>
""", unsafe_allow_html=True)
