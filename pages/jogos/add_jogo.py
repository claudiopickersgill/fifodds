import streamlit as st
import pandas as pd
from pages.conexao import conexao


def add_jogo():
    worksheet = conexao.faz_conexao()
    return worksheet


worksheet_raw = add_jogo()

# Function to find the last filled row in the worksheet.


def find_last_filled_row(worksheet):
    return len(worksheet.get_all_values()) + 1

# last = find_last_filled_row(worksheet)
# st.write(last)

    # values = df.values.tolist()
    # st.write(values)

# Function to insert data into the Google Sheet after the last filled row.


def insert_data_into_sheet(dataframe):
    # worksheet = worksheet_raw.get_worksheet(0)  # Replace 0 with the index of your desired worksheet
    values = dataframe.values.tolist()

    # Find the last filled row
    last_filled_row = find_last_filled_row(worksheet_raw)

    # Insert the data after the last filled row
    worksheet_raw.insert_rows(values, last_filled_row)


def interface():
    odd = st.number_input('Digite a Odd', key='odd')
    responsabilidade = st.number_input(
        'Digite a responsabilidade', key='responsabilidade')
    lucro = st.number_input('Digite o lucro', key='lucro')
    porcentagem = st.number_input('Digite a porcentagem', key='porcentagem')
    odd_equivalente = st.number_input(
        'Digite a Odd Equivalente', key='odd_equivalente')
    green = st.text_input('Aposta Vencedora? (Sim ou Não)', key='green')

    nova_linha = pd.DataFrame({'odd': [odd], 'responsabilidade': [responsabilidade], 'lucro': [
                              lucro], 'porcentagem': [porcentagem], 'odd_equivalente': [odd_equivalente], 'green': [green]})

    if st.button("Adicionar Linhas"):
        # Call the function to insert data into the Google Sheet
        insert_data_into_sheet(nova_linha)
        st.success("Linhas adicionadas com sucesso!")
