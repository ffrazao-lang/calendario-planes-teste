# Construção das linhas da tabela HTML sem indentação para o Markdown não tratar como bloco de código
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

# Cartão e tabela estilizados conforme o layout de referência
tabela_html = (
    '<div style="background-color: #F4F4F4; border-radius: 14px; padding: 20px 24px 26px 24px; '
    'box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08); font-family: sans-serif; margin-top: 10px;">'
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