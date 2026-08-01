import streamlit as st


def load_css():
    """Load custom CSS styles."""
    with open("styles/main.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def render_header(title: str, subtitle: str):
    """Render page header with title and subtitle."""
    st.markdown(f"""
    <div class="header">
        <h1>{title}</h1>
        <p>{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)


def render_result(emoji: str, label: str, confidence: float):
    """Render prediction result card."""
    st.markdown(f"""
    <div class="result-card">
        <div class="result-emoji">{emoji}</div>
        <div class="result-label">{label}</div>
        <div class="result-confidence">Confidence: {confidence*100:.1f}%</div>
    </div>
    """, unsafe_allow_html=True)


def render_team_card(name: str, role: str, linkedin: str = None):
    """Render team member card."""
    link = f'<a href="{linkedin}" target="_blank">🔗 LinkedIn</a>' if linkedin else ""
    st.markdown(f"""
    <div class="team-card">
        <div class="team-name">{name}</div>
        <div class="team-role">{role}</div>
        {link}
    </div>
    """, unsafe_allow_html=True)
