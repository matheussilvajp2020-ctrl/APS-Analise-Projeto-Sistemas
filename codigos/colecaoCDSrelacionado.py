import streamlit as st

class Musico:
    def __init__(self, nome):
        self.nome = nome

class Musica:
    def __init__(self, titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao

class CD:
    def __init__(self, titulo, ano, is_coletanea, is_duplo):
        self.titulo = titulo
        self.ano = ano
        self.is_coletanea = is_coletanea
        self.is_duplo = is_duplo
        self.musicas = []
        self.artistas = []

    def adicionar_musica(self, musica):
        self.musicas.append(musica)

    def adicionar_artista(self, musico):
        self.artistas.append(musico)

st.title("Gerenciador de Coleção de CDs")

titulo = st.text_input("Título do CD:")
ano = st.number_input("Ano:", 1900, 2026)
coletanea = st.checkbox("É coletânea?")
duplo = st.checkbox("É CD duplo?")

if st.button("Cadastrar CD"):
    st.session_state.cd_atual = CD(titulo, ano, coletanea, duplo)
    st.success("CD criado!")

if 'cd_atual' in st.session_state:
    nome_musica = st.text_input("Nome da música:")
    duracao = st.text_input("Duração (min:seg):")
    if st.button("Adicionar Música"):
        st.session_state.cd_atual.adicionar_musica(Musica(nome_musica, duracao))