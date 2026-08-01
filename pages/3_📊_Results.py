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

# ── Header ────────────────────────────────────────────────────────────────────
render_header(
    get_text("📊 Results", "📊 النتائج"),
    get_text(
        "View all your previous predictions in one place.",
        "اعرض كل التنبؤات السابقة في مكان واحد."
    )
)

st.divider()

history = st.session_state.get("history", [])

# ══════════════════════════════════════════════════════
# EMPTY STATE
# ══════════════════════════════════════════════════════
if not history:
    st.markdown(f"""
    <div class="no-history">
        <div class="no-history-icon">📭</div>
        <h3>{get_text("No predictions yet", "لا توجد تنبؤات بعد")}</h3>
        <p>{get_text(
            "Head to the Predict page and upload a traffic sign image to get started.",
            "اذهب لصفحة التنبؤ وارفع صورة إشارة مرور للبدء."
        )}</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        if st.button(
            get_text("🔍 Go to Predict", "🔍 اذهب للتنبؤ"),
            use_container_width=True,
            type="primary"
        ):
            st.switch_page("pages/2_🔍_Predict.py")

# ══════════════════════════════════════════════════════
# HISTORY
# ══════════════════════════════════════════════════════
else:
    total     = len(history)
    avg_conf  = sum(h["confidence"] for h in history) / total
    top_label = max(
        set(h["label"] for h in history),
        key=lambda x: sum(1 for h in history if h["label"] == x)
    )
    best_conf = max(h["confidence"] for h in history)

    # ── Stats row ─────────────────────────────────────
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric(get_text("Total Predictions", "إجمالي التنبؤات"), total)
    with c2:
        st.metric(get_text("Avg Confidence", "متوسط الثقة"), f"{avg_conf:.1f}%")
    with c3:
        st.metric(get_text("Best Score", "أعلى نتيجة"), f"{best_conf:.1f}%")
    with c4:
        st.metric(get_text("Most Predicted", "الأكثر تنبؤاً"), top_label)

    st.divider()

    # ── History cards ─────────────────────────────────
    st.markdown(f"### {get_text('🕓 Prediction History', '🕓 سجل التنبؤات')}")

    for i, entry in enumerate(reversed(history), start=1):
        conf = entry["confidence"]
        conf_color = (
            "var(--success)"  if conf >= 90 else
            "var(--warning)"  if conf >= 60 else
            "var(--accent)"
        )
        st.markdown(f"""
        <div class="history-card">
            <div class="history-emoji">{entry["emoji"]}</div>
            <div class="history-body">
                <div class="history-label">{entry["label"]}</div>
                <div class="history-meta">📁 {entry["image"]}</div>
            </div>
            <div class="history-conf" style="color:{conf_color};">{conf:.1f}%</div>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # ── DataFrame export ──────────────────────────────
    with st.expander(get_text("📋 View as Table", "📋 عرض كجدول"), expanded=False):
        df = pd.DataFrame(history)
        df.index += 1
        df.columns = [
            get_text("Image", "الصورة"),
            get_text("Label", "التصنيف"),
            get_text("Emoji", "الأيقونة"),
            get_text("Confidence %", "نسبة الثقة %"),
        ]
        st.dataframe(df, use_container_width=True)

        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label=get_text("⬇️ Download CSV", "⬇️ تحميل CSV"),
            data=csv,
            file_name="predictions.csv",
            mime="text/csv",
        )

    st.divider()

    # ── Clear ─────────────────────────────────────────
    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        if st.button(
            get_text("🗑️ Clear History", "🗑️ مسح السجل"),
            use_container_width=True
        ):
            st.session_state["history"] = []
            st.rerun()
