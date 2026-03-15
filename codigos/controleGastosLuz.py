import streamlit as st
import pandas as pd
from datetime import date

class ContaLuz:
    def __init__(self, data_leitura, num_leitura, kw_gasto, valor_pagar, data_pagamento, media_consumo):
        self.data_leitura = data_leitura
        self.num_leitura = num_leitura
        self.kw_gasto = kw_gasto
        self.valor_pagar = valor_pagar
        self.data_pagamento = data_pagamento
        self.media_consumo = media_consumo

st.title("Controle de Gastos: Conta de Luz")

if 'contas' not in st.session_state:
    st.session_state.contas = []

with st.form("cadastro_conta"):
    d_leitura = st.date_input("Data da Leitura")
    n_leitura = st.number_input("Número da Leitura", step=1)
    kw = st.number_input("KW Gasto", step=0.1)
    valor = st.number_input("Valor a Pagar (R$)", step=0.01)
    d_pagamento = st.date_input("Data do Pagamento")
    media = st.number_input("Média de Consumo", step=0.1)
    
    submitted = st.form_submit_button("Cadastrar Conta")
    if submitted:
        nova_conta = ContaLuz(d_leitura, n_leitura, kw, valor, d_pagamento, media)
        st.session_state.contas.append(vars(nova_conta))
        st.success("Conta cadastrada com sucesso!")

if st.session_state.contas:
    df = pd.DataFrame(st.session_state.contas)
    st.subheader("Lista de Contas")
    st.table(df)
    
    st.subheader("Análise de Consumo")
    col1, col2 = st.columns(2)
    
    with col1:
        mes_menor = df.loc[df['kw_gasto'].idxmin()]
        st.metric("Menor Consumo (KW)", mes_menor['kw_gasto'])
        st.write(f"Data: {mes_menor['data_leitura']}")
        
    with col2:
        mes_maior = df.loc[df['kw_gasto'].idxmax()]
        st.metric("Maior Consumo (KW)", mes_maior['kw_gasto'])
        st.write(f"Data: {mes_maior['data_leitura']}")