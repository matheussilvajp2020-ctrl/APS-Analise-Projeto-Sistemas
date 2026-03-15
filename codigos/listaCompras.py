import streamlit as st

class ItemCompra:
    def __init__(self, produto, unid, qtd_mes, qtd_compra, preco):
        self.produto = produto
        self.unid_compra = unid
        self.qtd_mes = qtd_mes
        self.qtd_compra = qtd_compra
        self.preco_estimado = preco

    def analisar_gasto(self):
        return self.qtd_compra * self.preco_estimado

st.title("Lista de Compras")

if 'itens' not in st.session_state:
    st.session_state.itens = []

prod = st.text_input("Produto:")
unid = st.text_input("Unidade (ex: Kg):")
qtd_m = st.number_input("Qtd Mês:", 0.0)
qtd_c = st.number_input("Qtd Compra:", 0.0)
preco = st.number_input("Preço Estimado:", 0.0)

if st.button("Adicionar Item"):
    item = ItemCompra(prod, unid, qtd_m, qtd_c, preco)
    st.session_state.itens.append(item)

if st.session_state.itens:
    for i in st.session_state.itens:
        st.write(f"{i.produto}: R$ {i.analisar_gasto():.2f}")