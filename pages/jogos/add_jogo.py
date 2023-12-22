import streamlit as st
import pandas as pd
from pages.jogos import cria_csv

# def add_rows(df, new_rows):
#     df = pd.concat([df, new_rows], ignore_index=True)
#     return df

def add_jogo():
    file_path = "data/cvs/Jogos.csv"
    if st.button("Carregar CSV"):
        df = cria_csv.read_csv(file_path)
        st.write("DataFrame Atual:")
        st.write(df)

    odd = st.number_input('Digite a Odd', key='odd')
    responsabilidade = st.number_input('Digite a Odd',key='responsabilidade')
    lucro = st.number_input('Digite a Odd',key='lucro')
    porcentagem = st.number_input('Digite a Odd',key='porcentagem')
    odd_equivalente = st.number_input('Digite a Odd',key='odd_equivalente')
    green = st.number_input('Digite a Odd',key='green')
    # # Adicionando novas linhas
    # st.header("Adicionar Novas Linhas:")
    # new_rows = st.text_area("Digite as novas linhas no formato CSV:", "")
    # new_rows = pd.read_csv(pd.compat.StringIO(new_rows)) if new_rows else pd.DataFrame()

    # if st.button("Adicionar Linhas"):
    #     df = add_rows(df, new_rows)
    #     st.write("DataFrame Atualizado:")
    #     st.write(df)
    #     df.to_csv(file_path, index=False)
    #     st.success("Linhas adicionadas com sucesso!")
