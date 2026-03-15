import streamlit as st

class CD:
    def __init__(self, artista, titulo, ano):
        self.artista = artista
        self.titulo = titulo
        self.ano_lancamento = ano

    def cadastrar_cd(self):
        return f"{self.titulo} de {self.artista} ({self.ano_lancamento})"

st.title("Coleção de CDs")

if 'cds' not in st.session_state:
    st.session_state.cds = []

art = st.text_input("Artista/Conjunto:")
tit = st.text_input("Título do CD:")
ano = st.number_input("Ano de Lançamento:", 1900, 2026)

if st.button("Cadastrar"):
    novo_cd = CD(art, tit, ano)
    st.session_state.cds.append(novo_cd)

if st.session_state.cds:
    st.write("Meus CDs:")
    for cd in st.session_state.cds:
        st.write(f"- {cd.cadastrar_cd()}")