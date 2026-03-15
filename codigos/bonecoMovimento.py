import streamlit as st

class Boneco:
    def __init__(self, nome, pos_x=0, pos_y=0, direcao="direita"):
        self.nome = nome
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.direcao = direcao

    def mover(self):
        if self.direcao == "cima": self.pos_y += 1
        elif self.direcao == "baixo": self.pos_y -= 1
        elif self.direcao == "direita": self.pos_x += 1
        elif self.direcao == "esquerda": self.pos_x -= 1

    def mudar_direcao(self, nova_direcao):
        self.direcao = nova_direcao

st.title("Boneco em Movimento")

if 'boneco' not in st.session_state:
    st.session_state.boneco = Boneco("Mário")

b = st.session_state.boneco

col1, col2 = st.columns(2)
with col1:
    nova_dir = st.selectbox("Mudar Direção", ["cima", "baixo", "esquerda", "direita"])
    if st.button("Mudar Direção"):
        b.mudar_direcao(nova_dir)
        st.rerun()

with col2:
    if st.button("Mover"):
        b.mover()
        st.rerun()

st.write(f"### {b.nome} está na posição ({b.pos_x}, {b.pos_y}) olhando para {b.direcao}")