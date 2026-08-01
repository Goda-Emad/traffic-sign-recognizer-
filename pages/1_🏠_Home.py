import streamlit as st
from components.sidebar import render_sidebar, get_text
from components.ui import load_css
from core.constants import CLASS_LABELS

st.set_page_config(
    page_title="Home 🏠",
    page_icon="🚦",
    layout="wide"
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
            "Upload any traffic sign photo — our MobileNet model classifies it instantly with high confidence.",
            "ارفع أي صورة إشارة مرور — موديل MobileNet يصنفها فوراً بدقة عالية."
        )}
    </p>
    <div class="hero-cta-row">
        <span class="tag">MobileNet</span>
        <span class="tag">TensorFlow</span>
        <span class="tag">Streamlit</span>
        <span class="tag">Python</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.divider()

# ── Stats ─────────────────────────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric(get_text("Model", "الموديل"), "MobileNet")
with c2:
    st.metric(get_text("Classes", "التصنيفات"), len(CLASS_LABELS))
with c3:
    st.metric(get_text("Training Images", "صور التدريب"), "6,390+")
with c4:
    st.metric(get_text("Accuracy", "الدقة"), "100%")

st.divider()

# ── How It Works ──────────────────────────────────────────────────────────────
st.markdown(f"### {get_text('⚙️ How It Works', '⚙️ كيف يعمل؟')}")

steps = [
    ("📤", get_text("Upload", "ارفع الصورة"),
     get_text("Upload any traffic sign image — JPG, JPEG, or PNG.",
              "ارفع أي صورة إشارة مرور بصيغة JPG أو PNG.")),
    ("🧠", get_text("Analyze", "التحليل"),
     get_text("MobileNet processes the image through deep neural layers.",
              "موديل MobileNet يحلل الصورة عبر طبقات الشبكة العصبية العميقة.")),
    ("✅", get_text("Predict", "النتيجة"),
     get_text("Get the predicted sign label with a confidence score.",
              "احصل على تصنيف الإشارة مع نسبة الثقة فوراً.")),
]

for i, (icon, title, desc) in enumerate(steps, start=1):
    col_num, col_content = st.columns([1, 11])
    with col_num:
        st.markdown(
            f"<div class='step-num'>0{i}</div>",
            unsafe_allow_html=True
        )
    with col_content:
        st.markdown(
            f"<div class='step-card'>"
            f"  <div class='step-icon'>{icon}</div>"
            f"  <div class='step-body'>"
            f"    <div class='step-title'>{title}</div>"
            f"    <div class='step-desc'>{desc}</div>"
            f"  </div>"
            f"</div>",
            unsafe_allow_html=True
        )

st.divider()

# ── Traffic Sign Classes ──────────────────────────────────────────────────────
st.markdown(f"### {get_text('🚸 Recognized Signs', '🚸 الإشارات المدعومة')}")

cols = st.columns(len(CLASS_LABELS))
for col, (emoji, label) in zip(cols, CLASS_LABELS):
    with col:
        st.markdown(
            f"<div class='sign-card'>"
            f"  <div class='sign-emoji'>{emoji}</div>"
            f"  <div class='sign-label'>{label}</div>"
            f"</div>",
            unsafe_allow_html=True
        )

st.divider()

# ── CTA ───────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="home-cta">
    <div class="cta-icon">🚀</div>
    <h3>{get_text("Ready to try it?", "جاهز تجرب؟")}</h3>
    <p>{get_text(
        "Head to the Predict page and upload your first traffic sign image.",
        "اذهب إلى صفحة التنبؤ وارفع أول صورة إشارة مرور."
    )}</p>
</div>
""", unsafe_allow_html=True)

st.page_link("pages/2_🔍_Predict.py",
             label=get_text("Go to Predict →", "ابدأ التنبؤ ←"),
             icon="🔍")
