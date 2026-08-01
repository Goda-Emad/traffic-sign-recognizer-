import streamlit as st


def render_sidebar():
    """Render sidebar with language and theme toggles."""

    with st.sidebar:

        st.markdown("""
        <div style='text-align:center; padding: 1rem 0;'>
            <h2 style='color:#E63946;'>🚦 Traffic Sign</h2>
            <p style='color:#888; font-size:0.8rem;'>Recognizer v1.0.0</p>
        </div>
        """, unsafe_allow_html=True)

        st.divider()

        # ── Language Toggle ──────────────────────────
        st.markdown("#### 🌐 Language / اللغة")
        lang = st.radio(
            label="lang",
            options=["🇬🇧 English", "🇪🇬 العربية"],
            horizontal=True,
            label_visibility="collapsed"
        )
        st.session_state["lang"] = "ar" if "العربية" in lang else "en"

        st.divider()

        # ── Theme Toggle ─────────────────────────────
        st.markdown("#### 🎨 Theme / المظهر")
        theme = st.radio(
            label="theme",
            options=["🌙 Dark", "☀️ Light"],
            horizontal=True,
            label_visibility="collapsed"
        )
        st.session_state["theme"] = "light" if "Light" in theme else "dark"

        # Apply theme CSS
        if st.session_state["theme"] == "light":
            st.markdown("""
            <style>
                .main { background-color: #F5F5F5 !important; }
                h1, h2, h3, p { color: #1A1A1A !important; }
                .result-card { background: #ffffff !important; border: 1px solid #ddd !important; }
                .team-card   { background: #ffffff !important; border: 1px solid #ddd !important; }
            </style>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <style>
                .main { background-color: #1A1A1A !important; }
                h1, h2, h3, p { color: #F1F1F1 !important; }
            </style>
            """, unsafe_allow_html=True)

        st.divider()

        # ── Navigation ───────────────────────────────
        st.markdown("#### 🗂️ Navigation" if st.session_state["lang"] == "en" else "#### 🗂️ الصفحات")
        st.page_link("app.py",            label="🏠 Home"    if st.session_state["lang"] == "en" else "🏠 الرئيسية")
        st.page_link("pages/2_🔍_Predict.py", label="🔍 Predict" if st.session_state["lang"] == "en" else "🔍 تنبؤ")
        st.page_link("pages/3_📊_Results.py", label="📊 Results" if st.session_state["lang"] == "en" else "📊 النتائج")
        st.page_link("pages/4_ℹ️_About.py",   label="ℹ️ About"   if st.session_state["lang"] == "en" else "ℹ️ عن المشروع")

        st.divider()

        st.markdown("<p style='text-align:center; color:#555; font-size:0.75rem;'>Made with ❤️ by Goda Emad</p>", unsafe_allow_html=True)


def get_text(en: str, ar: str) -> str:
    """Return text based on selected language."""
    lang = st.session_state.get("lang", "en")
    return ar if lang == "ar" else en
