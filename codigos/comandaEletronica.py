import streamlit as st

class Produto:
    def __init__(self, nome, valor_unitario):
        self.nome = nome
        self.valor_unitario = valor_unitario

class ItemComanda:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

class Comanda:
    def __init__(self, numero):
        self.numero = numero
        self.itens = []
        self.status = True

    def adicionar_item(self, produto, qtd):
        self.itens.append(ItemComanda(produto, qtd))

    def finalizar_compra(self):
        return sum(i.produto.valor_unitario * i.quantidade for i in self.itens)

st.title("Comanda Eletrônica")

if 'comanda' not in st.session_state:
    st.session_state.comanda = Comanda(101)

produto = st.text_input("Produto:")
valor = st.number_input("Valor Unitário:", 0.0)
qtd = st.number_input("Quantidade:", 1)

if st.button("Registrar Produto"):
    p = Produto(produto, valor)
    st.session_state.comanda.adicionar_item(p, qtd)
    st.success("Item adicionado!")

if st.button("Finalizar"):
    total = st.session_state.comanda.finalizar_compra()
    st.metric("Total da Compra", f"R$ {total:.2f}")