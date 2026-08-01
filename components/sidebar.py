# ═══════════════════════════════════════════════════════════════════
#  components/sidebar.py — Shared Sidebar
#  Traffic Sign Recognizer
# ═══════════════════════════════════════════════════════════════════
import streamlit as st

# ── Page definitions ─────────────────────────────────────────────
NAV = [
    ("🔍  Predict",  "🔍  تنبؤ",        "pages/2_🔍_Predict.py"),
    ("📊  Results",  "📊  النتائج",      "pages/3_📊_Results.py"),
    ("ℹ️  About",    "ℹ️  عن المشروع",   "pages/4_ℹ️_About.py"),
]


# ── Helper ───────────────────────────────────────────────────────
def get_text(en: str, ar: str) -> str:
    return ar if st.session_state.get("lang", "EN") == "AR" else en


# ── CSS injection ────────────────────────────────────────────────
def _inject_css():
    THEME = st.session_state.get("theme", "dark")
    LANG  = st.session_state.get("lang",  "EN")

    # ── Palette ───────────────────────────────────────────────────
    ACCENT  = "#E63946"
    GOLD    = "#E63946"   # keep brand consistent
    FF      = "Tajawal" if LANG == "AR" else "IBM Plex Sans"
    DIR     = "rtl"      if LANG == "AR" else "ltr"

    if THEME == "dark":
        NAV_BG  = "#1A1A1A"
        APP_BG  = "#1A1A1A"
        CARD_BG = "#2D2D2D"
        WHITE   = "#F1F1F1"
        GREY    = "#888888"
        BORDER  = "#3A3A3A"
        METRIC_BG = "#2D2D2D"
        METRIC_BORDER = "#3A3A3A"
        UPLOADER_BG = "#2D2D2D"
    else:
        NAV_BG  = "#EBEBEB"
        APP_BG  = "#F5F5F5"
        CARD_BG = "#FFFFFF"
        WHITE   = "#1A1A1A"
        GREY    = "#555555"
        BORDER  = "#DDDDDD"
        METRIC_BG = "#FFFFFF"
        METRIC_BORDER = "#DDDDDD"
        UPLOADER_BG = "#FFFFFF"

    st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;600;700&family=Tajawal:wght@400;700;800&display=swap');

/* ══ App background ══════════════════════════════════════ */
.stApp {{ background-color: {APP_BG} !important; }}

/* ══ Direction ═══════════════════════════════════════════ */
.stApp, .stApp p, .stApp h1, .stApp h2, .stApp h3,
.stApp span, .stMarkdown p {{
    direction: {DIR} !important;
    font-family: '{FF}', sans-serif !important;
    color: {WHITE} !important;
}}

/* ══ Sidebar shell ═══════════════════════════════════════ */
[data-testid="stSidebar"] {{
    background: {NAV_BG} !important;
    border-right: 1px solid {BORDER} !important;
}}
[data-testid="stSidebarNav"] {{ display: none !important; }}
[data-testid="stSidebar"] div,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label {{
    color: {WHITE} !important;
    font-family: '{FF}', sans-serif !important;
    direction: {DIR} !important;
}}

/* ══ ALL sidebar buttons — base style ═══════════════════ */
[data-testid="stSidebar"] .stButton > button {{
    background:    transparent !important;
    border:        1px solid transparent !important;
    color:         {GREY} !important;
    border-radius: 8px !important;
    width:         100% !important;
    font-size:     .88rem !important;
    font-weight:   500 !important;
    padding:       9px 14px !important;
    margin-bottom: 2px !important;
    text-align:    {DIR} !important;
    transition:    all .18s ease !important;
    font-family:   '{FF}', sans-serif !important;
}}
[data-testid="stSidebar"] .stButton > button:hover {{
    background:   {ACCENT}18 !important;
    color:        {ACCENT}   !important;
    border-color: {ACCENT}44 !important;
}}

/* ══ Theme / Language toggle buttons ════════════════════ */
.toggle-wrap .stButton > button {{
    background:    {CARD_BG} !important;
    border:        1px solid {BORDER} !important;
    color:         {WHITE} !important;
    font-weight:   600 !important;
    margin-bottom: 4px !important;
}}
.toggle-wrap .stButton > button:hover {{
    border-color: {ACCENT} !important;
    color:        {ACCENT}  !important;
}}

/* ══ Home button — accent tint ═══════════════════════════ */
.home-wrap .stButton > button {{
    background:    {ACCENT}18 !important;
    border:        1px solid {ACCENT}55 !important;
    color:         {ACCENT}  !important;
    font-weight:   700 !important;
    margin-bottom: 6px !important;
}}
.home-wrap .stButton > button:hover {{
    background:    {ACCENT}35 !important;
    border-color:  {ACCENT}  !important;
}}

/* ══ Nav buttons ═════════════════════════════════════════ */
.nav-wrap .stButton > button {{
    background:    {CARD_BG}   !important;
    border:        1px solid {BORDER} !important;
    color:         {WHITE}    !important;
    font-weight:   500 !important;
    margin-bottom: 3px !important;
}}
.nav-wrap .stButton > button:hover {{
    background:    {ACCENT}18 !important;
    border-color:  {ACCENT}55 !important;
    color:         {ACCENT}   !important;
}}

/* ══ Cards (result / team) ═══════════════════════════════ */
.result-card {{
    background:    {CARD_BG} !important;
    border:        1px solid {ACCENT} !important;
    border-radius: 16px !important;
    padding:       1.5rem 2rem !important;
    margin-bottom: 1rem !important;
    transition:    transform .2s ease, box-shadow .2s ease !important;
}}
.result-card:hover {{
    transform:  translateY(-3px) !important;
    box-shadow: 0 4px 20px {ACCENT}26 !important;
}}
.result-label      {{ color: {WHITE}  !important; font-size:1.8rem; font-weight:700; text-align:center; }}
.result-confidence {{ color: {ACCENT} !important; text-align:center; margin-top:.3rem; }}

.team-card {{
    background:    {CARD_BG} !important;
    border:        1px solid {BORDER} !important;
    border-radius: 12px !important;
    padding:       1.2rem !important;
    text-align:    center !important;
    transition:    transform .2s, border-color .2s !important;
}}
.team-card:hover {{ transform: translateY(-3px) !important; border-color: {ACCENT} !important; }}
.team-name {{ color: {WHITE}  !important; font-weight: 700; }}
.team-role {{ color: {GREY}   !important; font-size: .8rem; }}
.team-card a {{ color: {ACCENT} !important; text-decoration: none; font-weight: 600; }}

/* ══ Tag ═════════════════════════════════════════════════ */
.tag {{
    display:       inline-block;
    background:    {ACCENT}18;
    color:         {ACCENT};
    border-radius: 8px;
    padding:       .3rem .8rem;
    font-size:     .85rem;
    margin:        .2rem;
    font-weight:   600;
}}

/* ══ Metric ══════════════════════════════════════════════ */
[data-testid="stMetric"] {{
    background:    {METRIC_BG} !important;
    border:        1px solid {METRIC_BORDER} !important;
    border-radius: 12px !important;
    padding:       1rem !important;
}}
[data-testid="stMetricValue"] {{ color: {ACCENT} !important; font-weight: 700 !important; }}
[data-testid="stMetricLabel"] {{ color: {GREY}   !important; }}

/* ══ File uploader ═══════════════════════════════════════ */
[data-testid="stFileUploader"] {{
    background:    {UPLOADER_BG} !important;
    border:        2px dashed {ACCENT} !important;
    border-radius: 12px !important;
}}

/* ══ Main buttons ════════════════════════════════════════ */
.stApp .stButton > button {{
    background-color: {ACCENT} !important;
    color:            #fff !important;
    border:           none !important;
    border-radius:    8px !important;
    font-weight:      600 !important;
    transition:       opacity .2s ease !important;
}}
.stApp .stButton > button:hover {{ opacity: .88 !important; }}

/* ══ Divider / scrollbar ═════════════════════════════════ */
hr {{ border-color: {BORDER} !important; }}
::-webkit-scrollbar       {{ width: 6px; }}
::-webkit-scrollbar-track {{ background: {APP_BG}; }}
::-webkit-scrollbar-thumb {{ background: {ACCENT}; border-radius: 3px; }}

/* ══ Top header ══════════════════════════════════════════ */
header[data-testid="stHeader"] {{
    background-color: {CARD_BG} !important;
    border-bottom:    1px solid {BORDER} !important;
}}
header[data-testid="stHeader"] * {{ color: {WHITE} !important; }}
</style>
""", unsafe_allow_html=True)


# ── Divider helper ───────────────────────────────────────────────
def _divider(margin="10px 0"):
    BORDER = "#3A3A3A" if st.session_state.get("theme","dark") == "dark" else "#DDDDDD"
    st.markdown(
        f'<div style="height:1px;background:{BORDER};margin:{margin};"></div>',
        unsafe_allow_html=True,
    )


# ── Main render ──────────────────────────────────────────────────
def render_sidebar():
    if "theme" not in st.session_state: st.session_state.theme = "dark"
    if "lang"  not in st.session_state: st.session_state.lang  = "EN"

    THEME = st.session_state.theme
    LANG  = st.session_state.lang
    ACCENT = "#E63946"

    # inject CSS first so everything is themed before widgets render
    _inject_css()

    with st.sidebar:

        # ── Brand / Logo ──────────────────────────────────────
        name = "نظام التعرف على إشارات المرور" if LANG == "AR" else "Traffic Sign Recognizer"
        st.markdown(f"""
        <div style="display:flex;align-items:center;gap:10px;padding:16px 6px 14px;">
            <span style="font-size:2.2rem;line-height:1;">🚦</span>
            <div>
                <div style="font-size:.88rem;font-weight:700;">{name}</div>
                <div style="font-size:.58rem;color:{ACCENT};font-weight:600;
                            letter-spacing:1.1px;text-transform:uppercase;">
                    AI TRAFFIC SYSTEM
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        _divider("0 0 10px")

        # ── Theme toggle ──────────────────────────────────────
        thm_lbl = "☀️  Light" if THEME == "dark" else "🌙  Dark"
        st.markdown('<div class="toggle-wrap">', unsafe_allow_html=True)
        if st.button(thm_lbl, key="sb_theme", use_container_width=True):
            st.session_state.theme = "light" if THEME == "dark" else "dark"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

        # ── Language toggle ───────────────────────────────────
        lng_lbl = "🌐  العربية" if LANG == "EN" else "🌐  English"
        st.markdown('<div class="toggle-wrap">', unsafe_allow_html=True)
        if st.button(lng_lbl, key="sb_lang", use_container_width=True):
            st.session_state.lang = "AR" if LANG == "EN" else "EN"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

        _divider("8px 0")

        # ── Home button ───────────────────────────────────────
        home_lbl = "🏠  الرئيسية" if LANG == "AR" else "🏠  Home"
        st.markdown('<div class="home-wrap">', unsafe_allow_html=True)
        if st.button(home_lbl, key="sb_home", use_container_width=True):
            st.switch_page("app.py")
        st.markdown('</div>', unsafe_allow_html=True)

        _divider("4px 0 8px")

        # ── Navigation ────────────────────────────────────────
        st.markdown('<div class="nav-wrap">', unsafe_allow_html=True)
        for en_lbl, ar_lbl, fpath in NAV:
            label = ar_lbl if LANG == "AR" else en_lbl
            key   = "sb_nav_" + fpath.replace("/", "_").replace(".", "_")
            if st.button(label, key=key, use_container_width=True):
                st.switch_page(fpath)
        st.markdown('</div>', unsafe_allow_html=True)

        _divider("10px 0 8px")

        # ── Footer ────────────────────────────────────────────
        GREY = "#888" if THEME == "dark" else "#555"
        st.markdown(f"""
        <div style="font-size:.67rem;color:{GREY};padding:0 4px;line-height:2;">
            Made with ❤️ by Goda Emad
        </div>
        """, unsafe_allow_html=True)
