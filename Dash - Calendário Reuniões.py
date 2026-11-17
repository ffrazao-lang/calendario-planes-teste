import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# Título no padrão visual
st.markdown(
    "<h2 style='color: #E67E00; font-family: sans-serif;'>Acompanhamento das reuniões do Planes</h2>",
    unsafe_allow_html=True
)

# Dados baseados na página 4 do Guia Metodológico
dados_iniciais = pd.DataFrame([
    {"Oficina": "Oficina 1", "Etapa": "Identidade organizacional", "Início": "2026-11-02", "Fim": "2026-03-20"},
    {"Oficina": "Oficina 2", "Etapa": "Diagnóstico", "Início": "2026-03-06", "Fim": "2027-12-01"},
    {"Oficina": "Oficina 3", "Etapa": "Mapa Estratégico", "Início": "2027-06-16", "Fim": "2027-10-08"},
    {"Oficina": "Oficina 4", "Etapa": "Indicadores e metas", "Início": "2027-08-05", "Fim": "2027-12-07"},
    {"Oficina": "Oficina 5", "Etapa": "Projetos estratégicos", "Início": "2027-11-04", "Fim": "2027-06-04"},
])

# Tabela editável na barra lateral para alterar datas em tempo real
st.sidebar.header("Parâmetros do Cronograma")
df_editado = st.sidebar.data_editor(dados_iniciais, hide_index=True)

# Gráfico estilo Gantt
fig = px.timeline(
    df_editado,
    x_start="Início",
    x_end="Fim",
    y="Oficina",
    text="Etapa",
    color_discrete_sequence=["#F7C397"]
)

fig.update_yaxes(autorange="reversed", title="", showgrid=True, gridcolor="#D9D9D9")
fig.update_xaxes(title="", showgrid=True, gridcolor="#D9D9D9", tickformat="%b\n%Y")
fig.update_traces(textposition="inside", insidetextanchor="start", textfont=dict(color="#222222", size=13))
fig.update_layout(
    plot_bgcolor="white",
    paper_bgcolor="#F4F4F4",
    showlegend=False,
    height=420,
    margin=dict(l=20, r=20, t=20, b=20)
)

st.plotly_chart(fig, use_container_width=True)