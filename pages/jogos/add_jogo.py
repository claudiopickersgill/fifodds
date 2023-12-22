import streamlit as st
import pandas as pd
from pages.jogos import cria_csv

file_path = "data/cvs/Jogos.csv"

if st.button("Carregar CSV"):
        df = cria_csv.read_csv(file_path)
        st.write("DataFrame Atual:")
        st.write(df)

# def add_rows(df, nova_linha):
#     df = 
#     return df

def add_jogo():
    if st.button("Carregar CSV"):
        df = cria_csv.read_csv(file_path)
        st.write("DataFrame Atual:")
        st.write(df)

    odd = st.number_input('Digite a Odd', key='odd')
    responsabilidade = st.number_input('Digite a responsabilidade',key='responsabilidade')
    lucro = st.number_input('Digite a lucro',key='lucro')
    porcentagem = st.number_input('Digite a porcentagem',key='porcentagem')
    odd_equivalente = st.number_input('Digite a odd_equivalente',key='odd_equivalente')
    green = st.number_input('Digite a green',key='green')

    nova_linha = {'odd': [odd],
                  'responsabilidade': [responsabilidade],
                  'lucro': [lucro],
                  'porcentagem': [porcentagem],
                  'odd_equivalente': [odd_equivalente],
                  'green': [green]}
    df_nova_linha = pd.DataFrame(nova_linha)
    st.write(nova_linha)

    if st.button("Adicionar Linhas"):
        df = pd.concat([df, nova_linha], ignore_index=True)
        st.write("DataFrame Atualizado:")
        st.write(df)
        df_novo.to_csv(file_path, index=False)
        st.success("Linhas adicionadas com sucesso!")
