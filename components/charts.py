import streamlit as st
import plotly.graph_objects as go
from core.constants import CLASS_LABELS


def _theme_colors() -> dict:
    """Return color palette based on current theme."""
    if st.session_state.get("theme", "dark") == "light":
        return dict(
            paper_bg  = "#F5F5F5",
            plot_bg   = "#FFFFFF",
            font      = "#1A1A1A",
            grid      = "#DDDDDD",
            bar_other = "#E0E0E0",
            text_out  = "#1A1A1A",
            border    = "#FFFFFF",
        )
    else:
        return dict(
            paper_bg  = "#1A1A1A",
            plot_bg   = "#2D2D2D",
            font      = "#F1F1F1",
            grid      = "#3A3A3A",
            bar_other = "#3A3A3A",
            text_out  = "#F1F1F1",
            border    = "#1A1A1A",
        )


def render_confidence_bar(preds: list):
    """Horizontal bar chart — top predicted classes by confidence."""
    c = _theme_colors()

    labels = [CLASS_LABELS[i][1] for i in range(len(preds))]
    values = [float(p) * 100 for p in preds]
    max_v  = max(values) if values else 1
    colors = ["#E63946" if v == max_v else c["bar_other"] for v in values]

    fig = go.Figure(go.Bar(
        x            = values,
        y            = labels,
        orientation  = "h",
        marker       = dict(color=colors, line=dict(color=c["border"], width=0.3)),
        text         = [f"{v:.1f}%" for v in values],
        textposition = "outside",
        textfont     = dict(color=c["text_out"], size=12),
    ))

    fig.update_layout(
        title       = dict(text="Confidence per Class", font=dict(color=c["font"], size=14)),
        paper_bgcolor = c["paper_bg"],
        plot_bgcolor  = c["plot_bg"],
        font          = dict(color=c["font"]),
        xaxis = dict(
            title     = "Confidence %",
            range     = [0, 115],
            gridcolor = c["grid"],
            color     = c["font"],
            zerolinecolor = c["grid"],
        ),
        yaxis  = dict(title="", color=c["font"]),
        height = 320,
        margin = dict(l=10, r=20, t=45, b=10),
    )

    st.plotly_chart(fig, use_container_width=True)


def render_confidence_pie(preds: list):
    """Donut chart — confidence distribution across top classes."""
    c = _theme_colors()

    labels = [CLASS_LABELS[i][1] for i in range(len(preds))]
    values = [float(p) * 100 for p in preds]

    slice_colors = ["#E63946", "#FF6B6B", "#C1121F", "#780000", "#2D2D2D"]

    fig = go.Figure(go.Pie(
        labels     = labels,
        values     = values,
        marker     = dict(colors=slice_colors, line=dict(color=c["border"], width=2)),
        textfont   = dict(color=c["font"], size=12),
        hole       = 0.4,
        hovertemplate = "<b>%{label}</b><br>%{percent}<extra></extra>",
    ))

    fig.update_layout(
        title         = dict(text="Distribution of Confidence", font=dict(color=c["font"], size=14)),
        paper_bgcolor = c["paper_bg"],
        font          = dict(color=c["font"]),
        height        = 320,
        margin        = dict(l=10, r=10, t=45, b=10),
        legend        = dict(font=dict(color=c["font"])),
    )

    st.plotly_chart(fig, use_container_width=True)
