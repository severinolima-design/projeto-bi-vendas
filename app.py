import sqlite3
import pandas as pd
import streamlit as st

# ==========================================
# 1. BANCO DE DADOS (SQLite)
# ==========================================
def conectar_banco():
    conn = sqlite3.connect("vendas.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS vendas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT,
            produto TEXT,
            categoria TEXT,
            valor REAL
        )
    """
    )

    cursor.execute("SELECT COUNT(*) FROM vendas")
    if cursor.fetchone()[0] == 0:
        dados_iniciais = [
            ("2026-09-01", "Notebook", "Eletrônicos", 4500.00),
            ("2026-09-02", "Mouse", "Acessórios", 150.00),
            ("2026-09-03", "Teclado", "Acessórios", 250.00),
            ("2026-09-04", "Notebook", "Eletrônicos", 4500.00),
            ("2026-09-05", "Monitor", "Eletrônicos", 1200.00),
        ]
        cursor.executemany(
            "INSERT INTO vendas (data, produto, categoria, valor) VALUES (?, ?, ?, ?)",
            dados_iniciais,
        )
        conn.commit()

    conn.close()


conectar_banco()


def carregar_dados():
    conn = sqlite3.connect("vendas.db")
    df = pd.read_sql_query("SELECT * FROM vendas", conn)
    conn.close()
    return df


# ==========================================
# 2. FRONT-END E BACK-END (Streamlit)
# ==========================================
st.set_page_config(page_title="Dashboard de Vendas (BI)", layout="wide")

st.title("📊 Painel de Análise de Vendas - AC1")
st.markdown(
    "Integração completa: *Front-end (Streamlit)* | *Back-end (Python)* | *Banco de Dados (SQLite)*"
)

df = carregar_dados()

faturamento_total = df["valor"].sum()
st.metric("Faturamento Total", f"R$ {faturamento_total:,.2f}")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Tabela de Vendas (Banco de Dados SQLite)")
    st.dataframe(df, use_container_width=True)

with col2:
st.subheader("📈 Faturamento por Produto")
st.bar_chart(data=df, x="produto", y="valor")
# --- NOVA FUNCIONALIDADE PARA AC2: EXPORTAR DADOS ---
st.subheader("📥 Exportar Relatório de Vendas")

# Transforma os dados em CSV
csv = df.to_csv(index=False).encode('utf-8')

# Botão de download no Streamlit
st.download_button(
    label="Download do Relatório (CSV)",
    data=csv,
    file_name="relatorio_vendas_ac2.csv",
    mime="text/csv",
)
