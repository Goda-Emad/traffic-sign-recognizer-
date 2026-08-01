import streamlit as st
import plotly.graph_objects as go
from core.constants import CLASS_LABELS


def render_confidence_bar(preds):
    labels = [CLASS_LABELS[i][1] for i in range(len(preds))]
    values = [float(p) * 100 for p in preds]
    colors = ["#E63946" if v == max(values) else "#2D2D2D" for v in values]

    fig = go.Figure(go.Bar(
        x=values,
        y=labels,
        orientation="h",
        marker=dict(color=colors, line=dict(color="#F1F1F1", width=0.3)),
        text=[f"{v:.1f}%" for v in values],
        textposition="outside",
        textfont=dict(color="#F1F1F1")
    ))

    fig.update_layout(
        title="Confidence per Class",
        paper_bgcolor="#1A1A1A",
        plot_bgcolor="#2D2D2D",
        font=dict(color="#F1F1F1"),
        xaxis=dict(title="Confidence %", range=[0, 110], gridcolor="#3a3a3a"),
        yaxis=dict(title=""),
        height=300,
        margin=dict(l=10, r=10, t=40, b=10)
    )

    st.plotly_chart(fig, use_container_width=True)


def render_confidence_pie(preds):
    labels = [CLASS_LABELS[i][1] for i in range(len(preds))]
    values = [float(p) * 100 for p in preds]
    colors = ["#E63946", "#FF6B6B", "#C1121F", "#780000", "#2D2D2D"]

    fig = go.Figure(go.Pie(
        labels=labels,
        values=values,
        marker=dict(colors=colors, line=dict(color="#1A1A1A", width=2)),
        textfont=dict(color="#F1F1F1"),
        hole=0.4
    ))

    fig.update_layout(
        title="Distribution of Confidence",
        paper_bgcolor="#1A1A1A",
        font=dict(color="#F1F1F1"),
        height=300,
        margin=dict(l=10, r=10, t=40, b=10)
    )

    st.plotly_chart(fig, use_container_width=True)
