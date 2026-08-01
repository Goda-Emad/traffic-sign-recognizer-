import streamlit as st
from PIL import Image

from components.sidebar import render_sidebar, get_text
from components.ui import render_header, render_result, load_css
from components.predictor import predict
from components.charts import render_confidence_bar, render_confidence_pie
from core.constants import CLASS_LABELS

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Predict 🔍",
    page_icon="🔍",
    layout="wide"
)

load_css()
render_sidebar()

# ── Header ────────────────────────────────────────────────────────────────────
render_header(
    get_text("🔍 Predict", "🔍 تنبؤ"),
    get_text(
        "Upload a traffic sign image and get an instant AI prediction.",
        "ارفع صورة إشارة مرور واحصل على تنبؤ فوري بالذكاء الاصطناعي."
    )
)

st.divider()

# ── Upload zone ───────────────────────────────────────────────────────────────
uploaded_file = st.file_uploader(
    get_text("Upload a traffic sign image", "ارفع صورة إشارة مرور"),
    type=["jpg", "jpeg", "png"],
    help=get_text(
        "Supported formats: JPG, JPEG, PNG",
        "الصيغ المدعومة: JPG، JPEG، PNG"
    )
)

# ── Prediction flow ───────────────────────────────────────────────────────────
if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown(
            f"<p class='section-label'>"
            f"{get_text('Uploaded Image', 'الصورة المرفوعة')}"
            f"</p>",
            unsafe_allow_html=True
        )
        st.image(image, use_container_width=True)
        st.markdown(
            f"<p class='image-meta'>"
            f"📁 {uploaded_file.name} &nbsp;·&nbsp; "
            f"{image.width}×{image.height}px"
            f"</p>",
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"<p class='section-label'>"
            f"{get_text('Prediction', 'النتيجة')}"
            f"</p>",
            unsafe_allow_html=True
        )
        with st.spinner(get_text("Analyzing image…", "جاري تحليل الصورة…")):
            preds, top_idx, (emoji, label) = predict(image)

        confidence = float(preds[top_idx])
        render_result(emoji, label, confidence)

        # ── Confidence meter ──────────────────────────────────────────────
        st.markdown("<div class='conf-meter-wrap'>", unsafe_allow_html=True)
        st.progress(
            confidence,
            text=f"{get_text('Confidence', 'نسبة الثقة')}: **{confidence*100:.1f}%**"
        )
        st.markdown("</div>", unsafe_allow_html=True)

        # ── Quick stats row ───────────────────────────────────────────────
        rank = sorted(range(len(preds)), key=lambda i: preds[i], reverse=True).index(top_idx) + 1
        m1, m2, m3 = st.columns(3)
        m1.metric(get_text("Rank", "الترتيب"), f"#{rank}")
        m2.metric(get_text("Score", "النتيجة"), f"{confidence*100:.1f}%")
        m3.metric(get_text("Classes", "الفئات"), len(CLASS_LABELS))

        # ── Save to session history ───────────────────────────────────────
        if "history" not in st.session_state:
            st.session_state["history"] = []

        st.session_state["history"].append({
            "image":      uploaded_file.name,
            "label":      label,
            "emoji":      emoji,
            "confidence": confidence * 100,
        })

    st.divider()

    # ── Charts ────────────────────────────────────────────────────────────────
    st.markdown(
        f"### {get_text('📊 Confidence Analysis', '📊 تحليل نسب الثقة')}"
    )

    chart_col1, chart_col2 = st.columns([1, 1], gap="large")
    with chart_col1:
        render_confidence_bar(preds)
    with chart_col2:
        render_confidence_pie(preds)

    st.divider()

    # ── All probabilities table ───────────────────────────────────────────────
    st.markdown(
        f"### {get_text('📋 All Probabilities', '📋 جميع الاحتمالات')}"
    )

    sorted_preds = sorted(enumerate(preds), key=lambda x: x[1], reverse=True)

    for rank_pos, (idx, conf) in enumerate(sorted_preds, start=1):
        em, lbl = CLASS_LABELS[idx]
        is_top  = rank_pos == 1

        badge = (
            "<span class='top-badge'>TOP</span>" if is_top else
            f"<span class='rank-badge'>#{rank_pos}</span>"
        )

        col_a, col_b = st.columns([3, 1])
        with col_a:
            st.markdown(
                f"<div class='prob-label {'prob-label--top' if is_top else ''}'>"
                f"{badge} {em} {lbl}"
                f"</div>",
                unsafe_allow_html=True
            )
            st.progress(float(conf))
        with col_b:
            st.markdown(
                f"<div class='prob-pct {'prob-pct--top' if is_top else ''}'>"
                f"{conf*100:.1f}%"
                f"</div>",
                unsafe_allow_html=True
            )

# ── Empty state ───────────────────────────────────────────────────────────────
else:
    st.markdown(f"""
    <div class='empty-state'>
        <div class='empty-icon'>📂</div>
        <h3>{get_text("No image uploaded yet", "لم يتم رفع أي صورة بعد")}</h3>
        <p>{get_text(
            "Upload a traffic sign image above to get an instant AI prediction.",
            "ارفع صورة إشارة مرور للحصول على تنبؤ فوري بالذكاء الاصطناعي."
        )}</p>
        <div class='empty-hints'>
            <span class='tag'>JPG</span>
            <span class='tag'>JPEG</span>
            <span class='tag'>PNG</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
