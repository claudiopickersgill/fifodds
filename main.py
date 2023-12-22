import streamlit as st
from pages.principal import principal
from pages.odds import odds

st.set_page_config(layout="wide")

# Menu lateral
st.sidebar.title("Menu")
menu = st.sidebar.selectbox('Selecione uma Página', [
    'Principal', 'Calcular ODDS'])

if menu == 'Principal':
    principal.principal()
elif menu == 'Calcular ODDS':
    odds.odds()
