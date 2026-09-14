import streamlit as st
import pandas as pd

# Configuração inicial da página
st.set_page_config(page_title="Dashboard de Vendas", layout="wide")

# Título do projeto
st.title("📊 Painel de Análise de Vendas")
st.markdown("Projeto de Análise de Dados desenvolvido para a disciplina de Projeto de Software.")

# Dados simulados de vendas
dados = {
    "Data": ["2026-09-01", "2026-09-02", "2026-09-03", "2026-09-04", "2026-09-05"],
    "Produto": ["Notebook", "Mouse", "Teclado", "Notebook", "Monitor"],
    "Categoria": ["Eletrônicos", "Acessórios", "Acessórios", "Eletrônicos", "Eletrônicos"],
    "Valor": [4500, 150, 250, 4500, 1200]
}

df = pd.DataFrame(dados)

# Exibição de tabela e gráfico
st.subheader("📋 Tabela de Vendas Registradas")
st.dataframe(df)

st.subheader("📈 Faturamento por Produto")
st.bar_chart(data=df, x="Produto", y="Valor")
