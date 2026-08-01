import streamlit as st

PAGES = [
    {"icon": "🏠", "en": "Home",    "ar": "الرئيسية",   "path": "app.py"},
    {"icon": "🔍", "en": "Predict", "ar": "تنبؤ",        "path": "pages/2_🔍_Predict.py"},
    {"icon": "📊", "en": "Results", "ar": "النتائج",     "path": "pages/3_📊_Results.py"},
    {"icon": "ℹ️", "en": "About",   "ar": "عن المشروع",  "path": "pages/4_ℹ️_About.py"},
]


def get_text(en: str, ar: str) -> str:
    return ar if st.session_state.get("lang", "en") == "ar" else en


def _build_theme_css() -> str:
    theme  = st.session_state.get("theme", "dark")
    is_rtl = st.session_state.get("lang", "en") == "ar"

    if theme == "light":
        v = dict(
            bg_primary="#F5F5F5", bg_secondary="#FFFFFF", bg_card="#FFFFFF",
            bg_tertiary="#EEEEEE", border="#DDDDDD",
            accent="#E63946", accent_soft="rgba(230,57,70,0.09)",
            text="#1A1A1A", muted="#666666", faint="#999999",
            sidebar_bg="#EBEBEB",
        )
    else:
        v = dict(
            bg_primary="#1A1A1A", bg_secondary="#2D2D2D", bg_card="#2D2D2D",
            bg_tertiary="#3A3A3A", border="#3A3A3A",
            accent="#E63946", accent_soft="rgba(230,57,70,0.13)",
            text="#F1F1F1", muted="#888888", faint="#555555",
            sidebar_bg="#2D2D2D",
        )

    dir_val   = "rtl" if is_rtl else "ltr"
    align_val = "right" if is_rtl else "left"

    return f"""
<style>
/* ══ Variables ══════════════════════════════════════ */
:root {{
    --bg-primary:   {v['bg_primary']};
    --bg-secondary: {v['bg_secondary']};
    --bg-card:      {v['bg_card']};
    --bg-tertiary:  {v['bg_tertiary']};
    --border:       {v['border']};
    --accent:       {v['accent']};
    --accent-soft:  {v['accent_soft']};
    --text:         {v['text']};
    --muted:        {v['muted']};
    --faint:        {v['faint']};
}}

/* ══ App background ════════════════════════════════ */
.stApp {{ background-color: {v['bg_primary']} !important; }}

/* ══ Direction ═════════════════════════════════════ */
.stApp, .stMarkdown, .stApp p, .stApp span,
.stApp div, .stApp h1, .stApp h2, .stApp h3 {{
    direction: {dir_val};
    text-align: {align_val};
}}

/* ══ Global text ═══════════════════════════════════ */
.stApp p, .stApp span, .stApp li,
.stMarkdown p, .stMarkdown span, .stApp label {{
    color: {v['text']} !important;
}}
.stApp h1, .stApp h2, .stApp h3, .stApp h4 {{
    color: {v['text']} !important;
}}

/* ══ Sidebar ═══════════════════════════════════════ */
[data-testid="stSidebar"] {{
    background-color: {v['sidebar_bg']} !important;
    border-right: 1px solid {v['border']} !important;
}}
[data-testid="stSidebar"] * {{ color: {v['text']} !important; }}
[data-testid="stSidebarNav"] {{ display: none !important; }}

/* ══ Sidebar section cards ═════════════════════════ */
.sb-card {{
    background: {v['bg_card']} !important;
    border: 1px solid {v['border']} !important;
    border-radius: 14px !important;
    padding: 0.85rem 1rem 0.6rem !important;
    margin: 0 0 0.5rem 0 !important;
}}
.sb-card-title {{
    font-size: 0.78rem !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.06em !important;
    color: {v['muted']} !important;
    margin: 0 0 0.45rem 0 !important;
    display: block !important;
}}

/* ══ Radio inside sidebar ══════════════════════════ */
[data-testid="stSidebar"] .stRadio {{ margin: 0 !important; }}
[data-testid="stSidebar"] .stRadio label,
[data-testid="stSidebar"] .stRadio span {{
    color: {v['text']} !important;
    font-size: 0.88rem !important;
}}

/* ══ Nav page links ════════════════════════════════ */
[data-testid="stSidebar"] a[data-testid="stPageLink"] {{
    background: transparent !important;
    border-radius: 8px !important;
    padding: 0.35rem 0.6rem !important;
    margin-bottom: 0.1rem !important;
    display: flex !important;
    align-items: center !important;
    transition: background 0.15s ease !important;
}}
[data-testid="stSidebar"] a[data-testid="stPageLink"] span,
[data-testid="stSidebar"] a[data-testid="stPageLink"] p {{
    color: {v['text']} !important;
    font-weight: 500 !important;
    font-size: 0.9rem !important;
}}
[data-testid="stSidebar"] a[data-testid="stPageLink"]:hover {{
    background: {v['accent_soft']} !important;
}}
[data-testid="stSidebar"] a[data-testid="stPageLink"]:hover span,
[data-testid="stSidebar"] a[data-testid="stPageLink"]:hover p {{
    color: {v['accent']} !important;
}}

/* ══ Result / team cards ═══════════════════════════ */
.result-card {{
    background: {v['bg_card']} !important;
    border: 1px solid {v['accent']} !important;
    border-radius: 16px !important;
    padding: 1.5rem 2rem !important;
    margin-bottom: 1rem !important;
    transition: transform 0.2s ease, box-shadow 0.2s ease !important;
}}
.result-card:hover {{
    transform: translateY(-3px) !important;
    box-shadow: 0 4px 20px rgba(230,57,70,0.15) !important;
}}
.result-label      {{ color: {v['text']}   !important; font-size:1.8rem; font-weight:700; text-align:center; }}
.result-confidence {{ color: {v['accent']} !important; text-align:center; margin-top:0.3rem; }}

.team-card {{
    background: {v['bg_card']} !important;
    border: 1px solid {v['border']} !important;
    border-radius: 12px !important;
    padding: 1.2rem !important;
    text-align: center !important;
    transition: transform 0.2s, border-color 0.2s !important;
}}
.team-card:hover {{ transform: translateY(-3px) !important; border-color: {v['accent']} !important; }}
.team-name {{ color: {v['text']}   !important; font-weight: 700; }}
.team-role {{ color: {v['muted']}  !important; font-size: 0.8rem; }}
.team-card a {{ color: {v['accent']} !important; text-decoration: none; font-weight: 600; }}

/* ══ Tag ════════════════════════════════════════════ */
.tag {{
    display: inline-block;
    background: {v['accent_soft']};
    color: {v['accent']};
    border-radius: 8px;
    padding: 0.3rem 0.8rem;
    font-size: 0.85rem;
    margin: 0.2rem;
    font-weight: 600;
}}

/* ══ Metric ════════════════════════════════════════ */
[data-testid="stMetric"] {{
    background: {v['bg_card']} !important;
    border: 1px solid {v['border']} !important;
    border-radius: 12px !important;
    padding: 1rem !important;
}}
[data-testid="stMetricValue"] {{ color: {v['accent']} !important; font-weight: 700 !important; }}
[data-testid="stMetricLabel"] {{ color: {v['muted']}  !important; }}

/* ══ File uploader ═════════════════════════════════ */
[data-testid="stFileUploader"] {{
    background: {v['bg_card']} !important;
    border: 2px dashed {v['accent']} !important;
    border-radius: 12px !important;
}}

/* ══ Buttons ════════════════════════════════════════ */
.stButton > button {{
    background-color: {v['accent']} !important;
    color: #fff !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
    transition: opacity 0.2s ease !important;
}}
.stButton > button:hover {{ opacity: 0.88 !important; }}

/* ══ Divider / scrollbar ════════════════════════════ */
hr {{ border-color: {v['border']} !important; }}
::-webkit-scrollbar       {{ width: 6px; }}
::-webkit-scrollbar-track {{ background: {v['bg_primary']}; }}
::-webkit-scrollbar-thumb {{ background: {v['accent']}; border-radius: 3px; }}

/* ══ Top header bar (page names) ════════════════════ */
header[data-testid="stHeader"] {{
    background-color: {v['bg_secondary']} !important;
    border-bottom: 1px solid {v['border']} !important;
}}
header[data-testid="stHeader"] * {{ color: {v['text']} !important; }}

/* ══ Multipage tab nav (page names at top) ══════════ */
[data-testid="stMainMenu"] {{ color: {v['text']} !important; }}
nav[data-testid="stSidebarNav"] a span {{ color: {v['text']} !important; }}

/* Show page title in header */
[data-testid="stAppViewBlockContainer"] > div:first-child h1 {{
    display: block !important;
}}
</style>
"""


def _apply_theme():
    """Backward-compat alias."""
    st.markdown(_build_theme_css(), unsafe_allow_html=True)


def render_sidebar():
    # ── Init session state ────────────────────────────
    if "lang"  not in st.session_state: st.session_state["lang"]  = "en"
    if "theme" not in st.session_state: st.session_state["theme"] = "dark"

    with st.sidebar:

        # ── Logo ──────────────────────────────────────
        st.markdown("""
        <div style='text-align:center; padding:1.2rem 0 0.8rem;'>
            <div style='font-size:2.5rem; line-height:1;'>🚦</div>
            <h2 style='color:#E63946; margin:0.3rem 0 0;
                       font-size:1.1rem; font-weight:800; direction:ltr;'>
                Traffic Sign
            </h2>
            <p style='font-size:0.72rem; margin:0;'>Recognizer v1.0.0</p>
        </div>
        """, unsafe_allow_html=True)

        st.divider()

        # ══ LANGUAGE CARD ══════════════════════════════
        st.markdown("""
        <div class='sb-card'>
            <span class='sb-card-title'>🌐 Language / اللغة</span>
        </div>
        """, unsafe_allow_html=True)
        lang = st.radio(
            label="lang",
            options=["🇬🇧 English", "🇪🇬 العربية"],
            index=1 if st.session_state["lang"] == "ar" else 0,
            horizontal=True,
            label_visibility="collapsed",
            key="lang_radio",
        )
        st.session_state["lang"] = "ar" if "العربية" in lang else "en"

        st.divider()

        # ══ THEME CARD ═════════════════════════════════
        theme_label = get_text("Theme", "المظهر")
        st.markdown(f"""
        <div class='sb-card'>
            <span class='sb-card-title'>🎨 {theme_label}</span>
        </div>
        """, unsafe_allow_html=True)
        theme = st.radio(
            label="theme",
            options=["🌙 Dark", "☀️ Light"],
            index=1 if st.session_state["theme"] == "light" else 0,
            horizontal=True,
            label_visibility="collapsed",
            key="theme_radio",
        )
        st.session_state["theme"] = "light" if "Light" in theme else "dark"

        st.divider()

        # ══ NAVIGATION CARD ════════════════════════════
        nav_label = get_text("Navigation", "الصفحات")
        st.markdown(f"""
        <div class='sb-card'>
            <span class='sb-card-title'>🗂️ {nav_label}</span>
        </div>
        """, unsafe_allow_html=True)
        for page in PAGES:
            label = f"{page['icon']} {get_text(page['en'], page['ar'])}"
            st.page_link(page["path"], label=label)

        st.divider()

        # ── Footer ────────────────────────────────────
        made = get_text("Made with ❤️ by Goda Emad", "صنع بـ ❤️ بواسطة جودا عماد")
        st.markdown(
            f"<p style='text-align:center; font-size:0.72rem; direction:ltr;'>{made}</p>",
            unsafe_allow_html=True,
        )

    # ── Inject theme CSS over full page ───────────────
    st.markdown(_build_theme_css(), unsafe_allow_html=True)
