import streamlit as st

class Remedio:
    def __init__(self, nome_pessoa, nome_remedio, data_inicio, qtd_dias, vezes_dia, dosagem):
        self.nome_pessoa = nome_pessoa
        self.nome_remedio = nome_remedio
        self.data_inicio = data_inicio
        self.qtd_dias = qtd_dias
        self.vezes_dia = vezes_dia
        self.dosagem = dosagem

    def cadastrar(self):
        pass

    def sugerir_horarios(self):
        return [f"{i * (24 // self.vezes_dia)}:00" for i in range(self.vezes_dia)]

class PlanilhaHorarios:
    def __init__(self, remedio):
        self.remedio = remedio
        self.status_atraso = False

    def gerar_planilha(self):
        horarios = self.remedio.sugerir_horarios()
        st.write(f"Horários: {', '.join(horarios)}")

    def reorganizar_atraso(self):
        self.status_atraso = True
        st.warning("Planilha reorganizada devido a atraso.")

st.title("Controle de Remédios")

nome = st.text_input("Nome:")
remedio = st.text_input("Remédio:")
dias = st.number_input("Dias:", 1)
vezes = st.number_input("Vezes ao dia:", 1)

if st.button("Gerar Agenda"):
    r = Remedio(nome, remedio, "08/03/2026", dias, vezes, "500mg")
    p = PlanilhaHorarios(r)
    p.gerar_planilha()
    if st.button("Registrar Atraso"):
        p.reorganizar_atraso()
        