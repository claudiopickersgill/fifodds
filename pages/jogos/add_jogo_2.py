import streamlit as st
import pandas as pd
from pages.jogos import add_jogo
from pages.jogos import find_last_filled_row
from pages.jogos import insert_data_into_sheet

def add_jogos_2():
  odd = st.number_input('Digite a Odd', key='odd')
  responsabilidade = st.number_input('Digite a responsabilidade',key='responsabilidade')
  lucro = st.number_input('Digite a lucro',key='lucro')
  porcentagem = st.number_input('Digite a porcentagem',key='porcentagem')
  odd_equivalente = st.number_input('Digite a odd_equivalente',key='odd_equivalente')
  green = st.number_input('Digite a green',key='green')

  nova_linha = pd.DataFrame({'odd': [odd], 'responsabilidade': [responsabilidade], 'lucro': [lucro], 'porcentagem': [porcentagem], 'odd_equivalente': [odd_equivalente], 'green': [green]})

  if st.button("Adicionar Linhas"):
    # Call the function to insert data into the Google Sheet
    insert_data_into_sheet.insert_data_into_sheet(nova_linha)
        # df_novo = pd.concat([df, nova_linha], ignore_index=True)
        # st.write("DataFrame Atualizado:")
        # st.write(df_novo)
        # df_novo.to_csv(file_path, index=False)
    st.success("Linhas adicionadas com sucesso!")
