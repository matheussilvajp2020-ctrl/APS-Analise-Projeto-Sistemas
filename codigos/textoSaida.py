import streamlit as st

class TextoSaida:
    def __init__(self, tamanho_letra, cor_fonte, cor_fundo, tipo_componente):
        self.tamanho_letra = tamanho_letra
        self.cor_fonte = cor_fonte
        self.cor_fundo = cor_fundo
        self.tipo_componente = tipo_componente

    def exibir(self, texto_conteudo):
        style = f"""
        <style>
        .custom-box {{
            font-size: {self.tamanho_letra}px;
            color: {self.cor_fonte};
            background-color: {self.cor_fundo};
            padding: 10px;
            border-radius: 5px;
        }}
        </style>
        """
        st.markdown(style, unsafe_allow_html=True)
        
        if self.tipo_componente == "Label":
            st.markdown(f'<div class="custom-box">{texto_conteudo}</div>', unsafe_allow_html=True)
        elif self.tipo_componente == "Edit":
            st.text_input("Campo de Edição:", value=texto_conteudo, disabled=True)
        elif self.tipo_componente == "Memo":
            st.text_area("Campo de Texto (Memo):", value=texto_conteudo, height=100, disabled=True)

st.title("Configurador de TextoSaída")

texto = st.text_input("Digite o conteúdo do texto:")
tam = st.slider("Tamanho da Letra (px)", 10, 50, 20)
cor_f = st.selectbox("Cor da Fonte", ["black", "white", "blue", "yellow", "gray"])
cor_bg = st.selectbox("Cor do Fundo", ["white", "black", "blue", "yellow", "gray"])
tipo = st.selectbox("Tipo de Componente", ["Label", "Edit", "Memo"])

if st.button("Configurar e Exibir"):
    obj_texto = TextoSaida(tam, cor_f, cor_bg, tipo)
    obj_texto.exibir(texto)