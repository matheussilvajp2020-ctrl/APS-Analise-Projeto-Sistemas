import streamlit as st
import pandas as pd

class TipoGasto:
    def __init__(self, id_tipo, destino, obs):
        self.id_tipo = id_tipo
        self.destino = destino
        self.obs = obs

class Gasto:
    def __init__(self, id_gasto, nome, data_g, valor, tipo, forma_pagamento):
        self.id_gasto = id_gasto
        self.nome = nome
        self.data_g = data_g
        self.valor = valor
        self.tipo = tipo
        self.forma_pagamento = forma_pagamento

    def gerar_relatorio_mensal(self, lista_gastos):
        df = pd.DataFrame([vars(g) for g in lista_gastos])
        return df.groupby(['tipo', 'forma_pagamento'])['valor'].sum()

st.title("Controle de Gastos Diários")

if 'gastos' not in st.session_state:
    st.session_state.gastos = []

nome = st.text_input("Descrição do Gasto:")
valor = st.number_input("Valor:", min_value=0.0)
forma = st.selectbox("Forma de Pagamento", ["Dinheiro", "PIX", "Débito", "Crédito", "Ticket"])

if st.button("Adicionar"):
    novo_gasto = Gasto(len(st.session_state.gastos)+1, nome, "2026-03-08", valor, "Alimentação", forma)
    st.session_state.gastos.append(novo_gasto)
    st.success("Gasto registrado!")

if st.session_state.gastos:
    st.subheader("Relatório Mensal")
    relatorio = st.session_state.gastos[0].gerar_relatorio_mensal(st.session_state.gastos)
    st.write(relatorio)