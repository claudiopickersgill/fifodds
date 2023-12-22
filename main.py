import streamlit as st
from pages.principal import principal
from pages.odds import odds
from pages.jogos import add_jogo

st.set_page_config(layout="wide")

# Menu lateral
st.sidebar.title("Menu")
menu = st.sidebar.selectbox('Selecione uma Página', [
    'Principal', 'Calcular ODDS', 'Incluir Jogo na Base'])

if menu == 'Principal':
    principal.principal()
elif menu == 'Calcular ODDS':
    odds.odds()
elif manu == 'Incluir Jogo na Base':
    add_jogo.add_jogo()
