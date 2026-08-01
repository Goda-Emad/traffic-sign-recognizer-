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

# ── Header ────────────────────────────────────────────────────────────────────
render_header(
    get_text("ℹ️ About", "ℹ️ عن المشروع"),
    get_text(
        "Everything you need to know about this project.",
        "كل ما تحتاج معرفته عن هذا المشروع."
    )
)

st.divider()

# ── Project Overview ──────────────────────────────────────────────────────────
st.markdown(f"### {get_text('📌 Project Overview', '📌 نظرة عامة')}")

st.markdown(f"""
<div class="about-section">
    <p>{get_text(
        "Traffic Sign Recognizer is a Deep Learning web application that classifies traffic signs "
        "in real-time. The model was trained using Google Teachable Machine on the GTSRB dataset, "
        "achieving 100% confidence on clean traffic sign images.",
        "نظام التعرف على إشارات المرور هو تطبيق ويب للتعلم العميق يصنف إشارات المرور في الوقت الفعلي. "
        "تم تدريب الموديل باستخدام Google Teachable Machine على مجموعة بيانات GTSRB، "
        "محققاً دقة 100٪ على صور إشارات المرور الواضحة."
    )}</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ── Model Details ─────────────────────────────────────────────────────────────
st.markdown(f"### {get_text('🧠 Model Details', '🧠 تفاصيل الموديل')}")

col1, col2 = st.columns(2, gap="large")

model_rows_left = [
    (get_text("Architecture", "المعمارية"),    "MobileNet"),
    (get_text("Framework",    "الإطار"),       "TensorFlow / Keras"),
    (get_text("Input Size",   "حجم الإدخال"), "224 × 224 px"),
]
model_rows_right = [
    (get_text("Output",           "الإخراج"),          "5-class Softmax"),
    (get_text("Training Samples", "عينات التدريب"),   f"~6,390 {get_text('images','صورة')}"),
    (get_text("Dataset",          "مجموعة البيانات"), "GTSRB (Kaggle)"),
]

def _model_table(rows):
    rows_html = "".join(
        f"<tr>"
        f"  <td class='model-key'>{k}</td>"
        f"  <td class='model-val'>{v}</td>"
        f"</tr>"
        for k, v in rows
    )
    return f"<div class='about-section'><table class='model-table'>{rows_html}</table></div>"

with col1:
    st.markdown(_model_table(model_rows_left),  unsafe_allow_html=True)
with col2:
    st.markdown(_model_table(model_rows_right), unsafe_allow_html=True)

st.divider()

# ── Supported Classes ─────────────────────────────────────────────────────────
st.markdown(f"### {get_text('🎯 Supported Classes', '🎯 الفئات المدعومة')}")

cols = st.columns(len(CLASS_LABELS))
for col, (emoji, label) in zip(cols, CLASS_LABELS):
    with col:
        st.markdown(f"""
        <div class="sign-card">
            <div class="sign-emoji">{emoji}</div>
            <div class="sign-label">{label}</div>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# ── Tech Stack ────────────────────────────────────────────────────────────────
st.markdown(f"### {get_text('🛠️ Tech Stack', '🛠️ التقنيات المستخدمة')}")

techs = [
    ("🐍", "Python 3.9+"),
    ("🤖", "TensorFlow"),
    ("🧠", "Keras"),
    ("🌊", "Streamlit"),
    ("🖼️", "Pillow"),
    ("🔢", "NumPy"),
    ("📈", "Plotly"),
    ("🏫", "Teachable Machine"),
    ("🗂️", "GTSRB Dataset"),
]

pills_html = "".join(
    f"<span class='tech-pill'>{icon} {name}</span>"
    for icon, name in techs
)
st.markdown(f"<div style='margin-top:0.5rem;'>{pills_html}</div>", unsafe_allow_html=True)

st.divider()

# ── Team ──────────────────────────────────────────────────────────────────────
st.markdown(f"### {get_text('👥 Our Team', '👥 فريق العمل')}")

cols = st.columns(len(TEAM))
for col, member in zip(cols, TEAM):
    with col:
        render_team_card(
            name=member["name"],
            role=get_text(
                member["role"],
                "قائد الفريق ومطور الذكاء الاصطناعي"
                if member["role"] != "Member" else "عضو فريق"
            ),
            linkedin=member.get("linkedin")
        )

st.divider()

# ── Links ─────────────────────────────────────────────────────────────────────
st.markdown(f"### {get_text('🔗 Links', '🔗 روابط')}")

col1, col2, col3 = st.columns([1, 1, 4])
with col1:
    st.link_button(
        get_text("⭐ GitHub Repo", "⭐ GitHub"),
        GITHUB_URL,
        use_container_width=True
    )
with col2:
    st.link_button(
        get_text("📊 Dataset", "📊 مجموعة البيانات"),
        DATASET_URL,
        use_container_width=True
    )

st.markdown(f"""
<p class="about-footer">
    v{APP_VERSION} &nbsp;·&nbsp;
    {get_text("Made with ❤️ by Goda Emad", "صنع بـ ❤️ بواسطة قدا عماد")}
</p>
""", unsafe_allow_html=True)
