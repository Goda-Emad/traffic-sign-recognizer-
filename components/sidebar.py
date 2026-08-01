import streamlit as st

PAGES = [
    {"icon": "🏠", "en": "Home",    "ar": "الرئيسية",   "path": "app.py"},
    {"icon": "🔍", "en": "Predict", "ar": "تنبؤ",        "path": "pages/2_🔍_Predict.py"},
    {"icon": "📊", "en": "Results", "ar": "النتائج",     "path": "pages/3_📊_Results.py"},
    {"icon": "ℹ️", "en": "About",   "ar": "عن المشروع",  "path": "pages/4_ℹ️_About.py"},
]


def get_text(en: str, ar: str) -> str:
    return ar if st.session_state.get("lang", "en") == "ar" else en


def _apply_theme():
    """Inject CSS variables into <html> based on current theme."""
    theme = st.session_state.get("theme", "dark")
    is_rtl = st.session_state.get("lang", "en") == "ar"

    if theme == "light":
        vars_css = """
            --bg-primary:   #F5F5F5;
            --bg-secondary: #FFFFFF;
            --bg-tertiary:  #E8E8E8;
            --border-color: #DDDDDD;
            --accent:       #E63946;
            --accent-soft:  rgba(230,57,70,0.08);
            --text-primary: #1A1A1A;
            --text-muted:   #555555;
            --text-faint:   #888888;
        """
        app_bg = "#F5F5F5"
        sidebar_bg = "#EBEBEB"
    else:
        vars_css = """
            --bg-primary:   #1A1A1A;
            --bg-secondary: #2D2D2D;
            --bg-tertiary:  #3a3a3a;
            --border-color: #3a3a3a;
            --accent:       #E63946;
            --accent-soft:  rgba(230,57,70,0.13);
            --text-primary: #F1F1F1;
            --text-muted:   #888888;
            --text-faint:   #555555;
        """
        app_bg = "#1A1A1A"
        sidebar_bg = "#2D2D2D"

    direction = "rtl" if is_rtl else "ltr"

    st.markdown(f"""
    <style>
        /* ── CSS Variables ── */
        :root {{ {vars_css} }}

        /* ── Direction ── */
        .stApp, .stMarkdown, p, span, div, h1, h2, h3, h4 {{
            direction: {direction};
        }}

        /* ── App background ── */
        .stApp {{
            background-color: {app_bg} !important;
        }}

        /* ── Sidebar background ── */
        [data-testid="stSidebar"] {{
            background-color: {sidebar_bg} !important;
            border-right: 1px solid var(--border-color) !important;
        }}

        /* ── Hide default nav ── */
        [data-testid="stSidebarNav"] {{ display: none !important; }}

        /* ── Global text color ── */
        .stApp p,
        .stApp span,
        .stApp li,
        .stApp td,
        .stApp th,
        .stMarkdown p,
        .stMarkdown span {{
            color: var(--text-primary) !important;
        }}

        .stApp h1, .stApp h2, .stApp h3, .stApp h4 {{
            color: var(--text-primary) !important;
        }}

        /* ── Sidebar text ── */
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] span,
        [data-testid="stSidebar"] div,
        [data-testid="stSidebar"] label {{
            color: var(--text-primary) !important;
        }}

        /* ── Radio labels ── */
        .stRadio label, .stRadio span {{
            color: var(--text-primary) !important;
        }}

        /* ── Page link override ── */
        [data-testid="stSidebar"] a[data-testid="stPageLink"] span {{
            color: var(--text-primary) !important;
            font-weight: 500;
        }}
        [data-testid="stSidebar"] a[data-testid="stPageLink"]:hover span {{
            color: var(--accent) !important;
        }}
        [data-testid="stSidebar"] a[data-testid="stPageLink"] {{
            background: transparent !important;
            border-radius: 8px;
            padding: 0.3rem 0.5rem;
            transition: background 0.15s ease;
        }}
        [data-testid="stSidebar"] a[data-testid="stPageLink"]:hover {{
            background: var(--accent-soft) !important;
        }}

        /* ── Cards ── */
        .result-card {{
            background: var(--bg-secondary) !important;
            border: 1px solid var(--accent) !important;
            border-radius: 16px;
            padding: 1.5rem 2rem;
            margin-bottom: 1rem;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }}
        .result-card:hover {{
            transform: translateY(-3px);
            box-shadow: 0 4px 20px rgba(230,57,70,0.15);
        }}

        .sidebar-section {{
            background: var(--bg-tertiary) !important;
            border: 1px solid var(--border-color) !important;
            border-radius: 12px;
            padding: 0.75rem 0.9rem;
            margin: 0.4rem 0;
        }}

        /* ── Metric ── */
        [data-testid="stMetric"] {{
            background: var(--bg-secondary) !important;
            border: 1px solid var(--border-color) !important;
            border-radius: 12px;
            padding: 1rem;
        }}
        [data-testid="stMetricValue"] {{ color: var(--accent) !important; font-weight: 700 !important; }}
        [data-testid="stMetricLabel"] {{ color: var(--text-muted) !important; }}

        /* ── File uploader ── */
        [data-testid="stFileUploader"] {{
            background: var(--bg-secondary) !important;
            border: 2px dashed var(--accent) !important;
            border-radius: 12px;
        }}

        /* ── Buttons ── */
        .stButton > button {{
            background-color: var(--accent) !important;
            color: #ffffff !important;
            border: none !important;
            border-radius: 8px !important;
            font-weight: 600 !important;
        }}
        .stButton > button:hover {{
            opacity: 0.88 !important;
        }}

        /* ── Divider ── */
        hr {{ border-color: var(--border-color) !important; }}

        /* ── Scrollbar ── */
        ::-webkit-scrollbar {{ width: 6px; }}
        ::-webkit-scrollbar-track {{ background: var(--bg-primary); }}
        ::-webkit-scrollbar-thumb {{ background: var(--accent); border-radius: 3px; }}

        /* ── Team & tag ── */
        .team-card {{
            background: var(--bg-secondary) !important;
            border: 1px solid var(--border-color) !important;
            border-radius: 12px;
            padding: 1.2rem;
            text-align: center;
            transition: transform 0.2s, border-color 0.2s;
        }}
        .team-card:hover {{ transform: translateY(-3px); border-color: var(--accent) !important; }}
        .team-name  {{ color: var(--text-primary) !important; font-weight: 700; }}
        .team-role  {{ color: var(--text-muted)   !important; font-size: 0.8rem; }}
        .team-card a {{ color: var(--accent) !important; text-decoration: none; font-weight: 600; }}

        .tag {{
            display: inline-block;
            background: var(--accent-soft);
            color: var(--accent);
            border-radius: 8px;
            padding: 0.3rem 0.8rem;
            font-size: 0.85rem;
            margin: 0.2rem;
            font-weight: 600;
        }}
    </style>
    """, unsafe_allow_html=True)


def render_sidebar():
    # ── Init session state ────────────────────────────
    if "lang"  not in st.session_state: st.session_state["lang"]  = "en"
    if "theme" not in st.session_state: st.session_state["theme"] = "dark"

    with st.sidebar:

        # ── Logo ──────────────────────────────────────
        st.markdown("""
        <div style='text-align:center; padding:1.2rem 0 0.8rem;'>
            <div style='font-size:2.5rem; line-height:1;'>🚦</div>
            <h2 style='color:#E63946; margin:0.3rem 0 0; font-size:1.1rem; font-weight:800;'>
                Traffic Sign
            </h2>
            <p style='color:var(--text-muted); font-size:0.72rem; margin:0;'>Recognizer v1.0.0</p>
        </div>
        """, unsafe_allow_html=True)

        st.divider()

        # ── Language ──────────────────────────────────
        st.markdown(f"""
        <div class='sidebar-section'>
            <p style='margin:0 0 0.5rem; font-size:0.78rem; font-weight:700;
                      text-transform:uppercase; letter-spacing:0.05em;
                      color:var(--text-muted);'>
                🌐 {get_text('Language', 'اللغة')}
            </p>
        </div>
        """, unsafe_allow_html=True)

        lang_options = ["🇬🇧 English", "🇪🇬 العربية"]
        default_lang = 1 if st.session_state["lang"] == "ar" else 0
        lang = st.radio(
            label="lang",
            options=lang_options,
            index=default_lang,
            horizontal=True,
            label_visibility="collapsed",
            key="lang_radio"
        )
        st.session_state["lang"] = "ar" if "العربية" in lang else "en"

        st.divider()

        # ── Theme ─────────────────────────────────────
        st.markdown(f"""
        <div class='sidebar-section'>
            <p style='margin:0 0 0.5rem; font-size:0.78rem; font-weight:700;
                      text-transform:uppercase; letter-spacing:0.05em;
                      color:var(--text-muted);'>
                🎨 {get_text('Theme', 'المظهر')}
            </p>
        </div>
        """, unsafe_allow_html=True)

        theme_options = ["🌙 Dark", "☀️ Light"]
        default_theme = 1 if st.session_state["theme"] == "light" else 0
        theme = st.radio(
            label="theme",
            options=theme_options,
            index=default_theme,
            horizontal=True,
            label_visibility="collapsed",
            key="theme_radio"
        )
        st.session_state["theme"] = "light" if "Light" in theme else "dark"

        st.divider()

        # ── Navigation ────────────────────────────────
        st.markdown(f"""
        <div class='sidebar-section'>
            <p style='margin:0 0 0.5rem; font-size:0.78rem; font-weight:700;
                      text-transform:uppercase; letter-spacing:0.05em;
                      color:var(--text-muted);'>
                🗂️ {get_text('Navigation', 'الصفحات')}
            </p>
        </div>
        """, unsafe_allow_html=True)

        for page in PAGES:
            label = f"{page['icon']} {get_text(page['en'], page['ar'])}"
            st.page_link(page["path"], label=label)

        st.divider()

        # ── Footer ────────────────────────────────────
        st.markdown(
            "<p style='text-align:center; font-size:0.72rem; color:var(--text-faint);'>"
            f"Made with ❤️ by Goda Emad</p>",
            unsafe_allow_html=True
        )

    # Apply theme AFTER sidebar renders (so it covers full page)
    _apply_theme()
