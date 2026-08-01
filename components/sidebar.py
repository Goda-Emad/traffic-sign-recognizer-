import streamlit as st

# ── Pages Config ──────────────────────────────────────
PAGES = [
    {"icon": "🏠", "en": "Home",    "ar": "الرئيسية",  "path": "app.py"},
    {"icon": "🔍", "en": "Predict", "ar": "تنبؤ",       "path": "pages/2_🔍_Predict.py"},
    {"icon": "📊", "en": "Results", "ar": "النتائج",    "path": "pages/3_📊_Results.py"},
    {"icon": "ℹ️", "en": "About",   "ar": "عن المشروع", "path": "pages/4_ℹ️_About.py"},
]

# ── Light / Dark CSS ───────────────────────────────────
DARK_CSS = """
<style>
    .main                          { background-color: #1A1A1A !important; }
    .result-card, .team-card       { background: #2D2D2D !important; border: 1px solid #E63946 !important; }
    .result-label, .team-name      { color: #F1F1F1 !important; }
    .result-confidence, .team-role { color: #E63946 !important; }
    .header h1                     { color: #F1F1F1 !important; }
    .header p                      { color: #888 !important; }
    [data-testid="stSidebar"]      { background-color: #1A1A1A !important; border-right: 1px solid #2D2D2D; }
</style>
"""

LIGHT_CSS = """
<style>
    .main                          { background-color: #F5F5F5 !important; }
    .result-card, .team-card       { background: #ffffff !important; border: 1px solid #ddd !important; }
    .result-label, .team-name      { color: #1A1A1A !important; }
    .result-confidence, .team-role { color: #E63946 !important; }
    .header h1                     { color: #1A1A1A !important; }
    .header p                      { color: #555 !important; }
    p, li, span, td, th            { color: #1A1A1A !important; }
    h1, h2, h3, h4                 { color: #1A1A1A !important; }
    [data-testid="stSidebar"]      { background-color: #ebebeb !important; border-right: 1px solid #ddd; }
    [data-testid="stMetricValue"]  { color: #E63946 !important; }
</style>
"""


def get_text(en: str, ar: str) -> str:
    """Return text based on selected language."""
    return ar if st.session_state.get("lang", "en") == "ar" else en


def render_sidebar():
    """Render sidebar with language, theme toggles and navigation."""

    # ── Init session defaults ──────────────────────────
    if "lang"  not in st.session_state: st.session_state["lang"]  = "en"
    if "theme" not in st.session_state: st.session_state["theme"] = "dark"

    with st.sidebar:

        # ── Logo ───────────────────────────────────────
        st.markdown("""
        <div style='text-align:center; padding:1rem 0;'>
            <div style='font-size:2.5rem;'>🚦</div>
            <h2 style='color:#E63946; margin:0;'>Traffic Sign</h2>
            <p style='color:#888; font-size:0.75rem; margin:0;'>Recognizer v1.0.0</p>
        </div>
        """, unsafe_allow_html=True)

        st.divider()

        # ── Language ───────────────────────────────────
        st.markdown(f"#### 🌐 {get_text('Language', 'اللغة')}")
        lang = st.radio(
            label="lang",
            options=["🇬🇧 English", "🇪🇬 العربية"],
            horizontal=True,
            label_visibility="collapsed"
        )
        st.session_state["lang"] = "ar" if "العربية" in lang else "en"

        st.divider()

        # ── Theme ──────────────────────────────────────
        st.markdown(f"#### 🎨 {get_text('Theme', 'المظهر')}")
        theme = st.radio(
            label="theme",
            options=["🌙 Dark", "☀️ Light"],
            horizontal=True,
            label_visibility="collapsed"
        )
        st.session_state["theme"] = "light" if "Light" in theme else "dark"
        st.markdown(LIGHT_CSS if st.session_state["theme"] == "light" else DARK_CSS, unsafe_allow_html=True)

        st.divider()

        # ── Navigation Cards ───────────────────────────
        st.markdown(f"#### 🗂️ {get_text('Navigation', 'الصفحات')}")

        for page in PAGES:
            label = f"{page['icon']} {get_text(page['en'], page['ar'])}"
            st.page_link(page["path"], label=label)

        st.divider()

        # ── Footer ─────────────────────────────────────
        st.markdown(
            "<p style='text-align:center; color:#555; font-size:0.75rem;'>Made with ❤️ by Goda Emad</p>",
            unsafe_allow_html=True
        )
