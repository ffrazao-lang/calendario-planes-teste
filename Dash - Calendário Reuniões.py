import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# Título principal
st.markdown(
    "<h2 style='color: #E67E00; font-family: sans-serif; margin-bottom: 10px;'>Acompanhamento das reuniões do Planes</h2>",
    unsafe_allow_html=True
)

# Dados completos (Guia Metodológico + Datas do cronograma)
dados_iniciais = pd.DataFrame([
    {
        "Oficina": "Oficina 1",
        "Etapa": "Identidade Organizacional",
        "Principal Objetivo": "Promover uma reflexão coletiva sobre a atuação e a identidade local, alinhando seus diferenciais e sua contribuição estratégica para a Universidade.",
        "Resultado Esperado": "Definição da identidade organizacional composta por missão, visão de futuro, princípios e valores.",
        "Início": "2026-11-02",
        "Fim": "2027-03-20"
    },
    {
        "Oficina": "Oficina 2",
        "Etapa": "Diagnóstico",
        "Principal Objetivo": "Realizar uma análise detalhada do cenário local com avaliação dos ambientes internos e externos.",
        "Resultado Esperado": "Definição dos pontos fortes, fracos, oportunidades e ameaças locais (Matriz SWOT), servindo de base para os objetivos estratégicos.",
        "Início": "2027-03-06",
        "Fim": "2027-06-15"
    },
    {
        "Oficina": "Oficina 3",
        "Etapa": "Mapa Estratégico",
        "Principal Objetivo": "Definir a estratégia local a partir dos resultados gerados pela análise dos pontos fortes, fracos, ameaças e oportunidades, estabelecendo as entregas necessárias para o alcance da visão.",
        "Resultado Esperado": "Construção do Mapa Estratégico contendo os objetivos alocados nas perspectivas do Planejamento Estratégico da Universidade.",
        "Início": "2027-06-16",
        "Fim": "2027-10-08"
    },
    {
        "Oficina": "Oficina 4",
        "Etapa": "Indicadores Estratégicos e Metas",
        "Principal Objetivo": "Definir a forma de medir a evolução do objetivo estratégico e qual o valor que se quer alcançar até o fim do período de vigência do Planes.",
        "Resultado Esperado": "Lista dos indicadores, seus métodos de cálculo e a meta numérica, relacionados a cada objetivo estratégico disponível no mapa local.",
        "Início": "2027-08-05",
        "Fim": "2027-12-07"
    },
    {
        "Oficina": "Oficina 5",
        "Etapa": "Projetos Estratégicos",
        "Principal Objetivo": "Estabelecer a estratégia de alcance das metas e traduzi-la no desenho de projetos, garantindo a concretização dos objetivos estratégicos.",
        "Resultado Esperado": "Projetos estratégicos que serão desenvolvidos localmente para desenvolvimento do Planes local e alcance da visão.",
        "Início": "2027-11-04",
        "Fim": "2028-06-04"
    },
])

# Tabela editável na barra lateral para alterar datas em tempo real
st.sidebar.header("Parâmetros do Cronograma")
df_editado = st.sidebar.data_editor(
    dados_iniciais[["Oficina", "Etapa", "Início", "Fim"]],
    hide_index=True
)

# Atualiza as datas na tabela completa caso o usuário edite na barra lateral
dados_completos = dados_iniciais.copy()
dados_completos["Início"] = df_editado["Início"]
dados_completos["Fim"] = df_editado["Fim"]

# Formata as datas para o padrão brasileiro (DD/MM/AAAA) na tabela visual
def formatar_data(data_str):
    try:
        return pd.to_datetime(data_str).strftime("%d/%m/%Y")
    except Exception:
        return data_str

# 1. TABELA ESTILIZADA (EXIBIDA PRIMEIRO)
linhas_html = ""
for idx, row in dados_completos.iterrows():
    bg_color = "#F4F4F4" if idx % 2 == 0 else "#FAFAFA"
    inicio_fmt = formatar_data(row["Início"])
    fim_fmt = formatar_data(row["Fim"])
    
    linhas_html += (
        f'<tr style="background-color: {bg_color}; border-bottom: 1px solid #E6E6E6;">'
        f'<td style="padding: 12px 14px; font-weight: bold; color: #222222; vertical-align: top; width: 16%;">{row["Oficina"]}: {row["Etapa"]}</td>'
        f'<td style="padding: 12px 14px; color: #333333; vertical-align: top; width: 34%;">{row["Principal Objetivo"]}</td>'
        f'<td style="padding: 12px 14px; color: #333333; vertical-align: top; width: 32%;">{row["Resultado Esperado"]}</td>'
        f'<td style="padding: 12px 14px; color: #333333; vertical-align: top; width: 9%; white-space: nowrap;">{inicio_fmt}</td>'
        f'<td style="padding: 12px 14px; color: #333333; vertical-align: top; width: 9%; white-space: nowrap;">{fim_fmt}</td>'
        f'</tr>'
    )

tabela_html = (
    '<div style="background-color: #F4F4F4; border-radius: 14px; padding: 20px 24px 26px 24px; '
    'box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08); font-family: sans-serif; margin-bottom: 24px;">'
    '<h3 style="color: #E67E00; margin-top: 0; margin-bottom: 14px; font-size: 22px; font-weight: 700;">'
    'Reuniões por objetivo estratégico e cronograma</h3>'
    '<table style="width: 100%; border-collapse: collapse; font-size: 13.5px; text-align: left;">'
    '<thead><tr style="background-color: #F58200; color: #000000;">'
    '<th style="padding: 10px 14px; font-weight: 700;">Reunião / Oficina</th>'
    '<th style="padding: 10px 14px; font-weight: 700;">Principal Objetivo</th>'
    '<th style="padding: 10px 14px; font-weight: 700;">Resultado Esperado</th>'
    '<th style="padding: 10px 14px; font-weight: 700;">Início</th>'
    '<th style="padding: 10px 14px; font-weight: 700;">Fim</th>'
    '</tr></thead>'
    f'<tbody>{linhas_html}</tbody>'
    '</table></div>'
)

st.markdown(tabela_html, unsafe_allow_html=True)

# 2. GRÁFICO DE GANTT (EXIBIDO ABAIXO DA TABELA)
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
    height=380,
    margin=dict(l=20, r=20, t=20, b=20)
)

st.plotly_chart(fig, use_container_width=True)