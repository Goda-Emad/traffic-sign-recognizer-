import streamlit as st
from components.sidebar import render_sidebar, get_text
from components.ui import render_header, render_team_card, load_css
from core.config import APP_VERSION, GITHUB_URL, DATASET_URL, TEAM
from core.constants import CLASS_LABELS

st.set_page_config(
    page_title="About ℹ️",
    page_icon="ℹ️",
    layout="wide"
)

load_css()
render_sidebar()

# ── Header ────────────────────────────────────────────
render_header(
    get_text("ℹ️ About", "ℹ️ عن المشروع"),
    get_text(
        "Everything you need to know about this project.",
        "كل ما تحتاج معرفته عن هذا المشروع."
    )
)

st.divider()

# ── Project Overview ──────────────────────────────────
st.markdown(f"### {get_text('📌 Project Overview', '📌 نظرة عامة')}")
st.markdown(f"""
<div class='result-card'>
    <p style='color:#ccc; line-height:1.9; font-size:1rem;'>
        {get_text(
            "Traffic Sign Recognizer is a Deep Learning web application that classifies traffic signs in real-time. "
            "The model was trained using Google Teachable Machine on the GTSRB dataset, "
            "achieving 100% confidence on clean traffic sign images.",
            "نظام التعرف على إشارات المرور هو تطبيق ويب للتعلم العميق يصنف إشارات المرور في الوقت الفعلي. "
            "تم تدريب الموديل باستخدام Google Teachable Machine على مجموعة بيانات GTSRB، "
            "محققاً دقة 100% على صور إشارات المرور الواضحة."
        )}
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ── Model Details ─────────────────────────────────────
st.markdown(f"### {get_text('🧠 Model Details', '🧠 تفاصيل الموديل')}")

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class='result-card'>
        <table style='color:#ccc; width:100%; border-collapse:collapse;'>
            <tr><td style='padding:0.5rem 0;'><b>{get_text("Architecture", "المعمارية")}</b></td><td>MobileNet</td></tr>
            <tr><td style='padding:0.5rem 0;'><b>{get_text("Framework", "الإطار")}</b></td><td>TensorFlow / Keras</td></tr>
            <tr><td style='padding:0.5rem 0;'><b>{get_text("Input Size", "حجم الإدخال")}</b></td><td>224 × 224 px</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class='result-card'>
        <table style='color:#ccc; width:100%; border-collapse:collapse;'>
            <tr><td style='padding:0.5rem 0;'><b>{get_text("Output", "الإخراج")}</b></td><td>5-class Softmax</td></tr>
            <tr><td style='padding:0.5rem 0;'><b>{get_text("Training Samples", "عينات التدريب")}</b></td><td>~6,390 {get_text("images", "صورة")}</td></tr>
            <tr><td style='padding:0.5rem 0;'><b>{get_text("Dataset", "مجموعة البيانات")}</b></td><td>GTSRB (Kaggle)</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ── Supported Classes ─────────────────────────────────
st.markdown(f"### {get_text('🎯 Supported Classes', '🎯 الفئات المدعومة')}")

cols = st.columns(5)
for i, (emoji, label) in CLASS_LABELS.items():
    with cols[i]:
        st.markdown(f"""
        <div class='result-card' style='text-align:center; padding:1rem;'>
            <div style='font-size:2rem;'>{emoji}</div>
            <p style='color:#F1F1F1; font-size:0.85rem; margin-top:0.5rem;'>{label}</p>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# ── Tech Stack ────────────────────────────────────────
st.markdown(f"### {get_text('🛠️ Tech Stack', '🛠️ التقنيات المستخدمة')}")

tags = ["Python 3.9+", "TensorFlow", "Keras", "Streamlit", "Pillow", "NumPy", "Plotly", "Teachable Machine", "GTSRB Dataset"]
tags_html = "".join([f"<span class='tag'>{t}</span>" for t in tags])
st.markdown(f"<div style='margin-top:0.5rem;'>{tags_html}</div>", unsafe_allow_html=True)

st.divider()

# ── Team ──────────────────────────────────────────────
st.markdown(f"### {get_text('👥 Our Team', '👥 فريق العمل')}")

cols = st.columns(len(TEAM))
for i, member in enumerate(TEAM):
    with cols[i]:
        render_team_card(
            name=member["name"],
            role=get_text(member["role"], "عضو فريق" if member["role"] == "Member" else "قائد الفريق ومطور الذكاء الاصطناعي"),
            linkedin=member["linkedin"]
        )

st.divider()

# ── Links ─────────────────────────────────────────────
st.markdown(f"### {get_text('🔗 Links', '🔗 روابط')}")

col1, col2, col3 = st.columns([1, 1, 4])
with col1:
    st.link_button(get_text("⭐ GitHub Repo", "⭐ GitHub"), GITHUB_URL, use_container_width=True)
with col2:
    st.link_button(get_text("📊 Dataset", "📊 مجموعة البيانات"), DATASET_URL, use_container_width=True)

st.markdown(
    f"<p style='text-align:center; color:#555; margin-top:2rem;'>v{APP_VERSION} • {get_text('Made with ❤️ by Goda Emad', 'صنع بـ ❤️ بواسطة قدا عماد')}</p>",
    unsafe_allow_html=True
)
