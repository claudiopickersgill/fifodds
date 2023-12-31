import streamlit as st
from pages.principal import principal
from pages.odds import odds
from pages.jogos import add_jogo
from pages.jogos import add_jogo_2
from pages.pagina_teste import pagina_teste

# Menu lateral
st.sidebar.title("Menu")
menu = st.sidebar.selectbox('Selecione uma Página', [
    'Principal', 'Calcular ODDS', 'Incluir Jogo na Base', 'Pagina Teste', 'Add Jogo'])

if menu == 'Principal':
    principal.principal()
elif menu == 'Calcular ODDS':
    odds.odds()
elif menu == 'Incluir Jogo na Base':
    add_jogo.add_jogo()
elif menu == 'Pagina Teste':
    pagina_teste.teste()
elif menu == 'Add Jogo':
    add_jogo_2.add_jogo_2()
