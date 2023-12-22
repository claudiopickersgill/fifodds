import streamlit as st
from pages.odds import odds

st.set_page_config(layout="wide")

# Menu lateral
st.sidebar.title("Menu")
menu = st.sidebar.selectbox('Selecione uma Página', [
    'Calcular ODDS'])

if menu == 'Calcular ODDS':
    odds.odds()
