import streamlit as st

class Base:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class ContaLuz(Base):
    def __init__(self, id, nome, kw, valor):
        super().__init__(id, nome)
        self.kw = kw
        self.valor = valor

class Remedio(Base):
    def __init__(self, id, nome, dosagem):
        super().__init__(id, nome)
        self.dosagem = dosagem

st.title("Sistema Baseado em Herança")

if 'itens' not in st.session_state:
    st.session_state.itens = []

tipo = st.selectbox("Tipo:", ["Conta de Luz", "Remédio"])
nome = st.text_input("Nome/Descrição:")

if st.button("Cadastrar"):
    if tipo == "Conta de Luz":
        item = ContaLuz(len(st.session_state.itens)+1, nome, 100, 50.0)
    else:
        item = Remedio(len(st.session_state.itens)+1, nome, "500mg")
    
    st.session_state.itens.append(item)
    st.success(f"{tipo} cadastrado com ID {item.id}")