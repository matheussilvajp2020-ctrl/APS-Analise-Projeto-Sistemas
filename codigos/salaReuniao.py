import streamlit as st
from datetime import datetime

class Reserva:
    def __init__(self, data, hora, solicitante):
        self.data = data
        self.hora = hora
        self.solicitante = solicitante

class Sala:
    def __init__(self, numero, capacidade):
        self.numero = numero
        self.capacidade = capacidade
        self.reservas = []

    def verificar_disponibilidade(self, data, hora):
        for r in self.reservas:
            if r.data == data and r.hora == hora:
                return False
        return True

    def adicionar_reserva(self, reserva):
        self.reservas.append(reserva)

st.title("Gestão de Sala de Reunião")

if 'sala' not in st.session_state:
    st.session_state.sala = Sala(101, 20)

data = st.date_input("Data:")
hora = st.time_input("Hora:")
nome = st.text_input("Solicitante:")

if st.button("Reservar"):
    if st.session_state.sala.verificar_disponibilidade(data, hora):
        nova_reserva = Reserva(data, hora, nome)
        st.session_state.sala.adicionar_reserva(nova_reserva)
        st.success("Reserva confirmada!")
    else:
        st.error("Horário indisponível!")