import streamlit as st
from pages.principal import principal
from pages.odds import odds
from pages.jogos import add_jogo
from pages.graficos import graficos

# Menu lateral
st.sidebar.title("Menu")
menu = st.sidebar.selectbox('Selecione uma Página', [
    'Principal', 'Calcular ODDS', 'Adicionar Jogo na Base', 'Gráficos'])

if menu == 'Principal':
    principal.principal()
elif menu == 'Calcular ODDS':
    odds.odds()
elif menu == 'Adicionar Jogo na Base':
    add_jogo.interface()
elif menu == 'Gráficos':
    graficos.graficos()
