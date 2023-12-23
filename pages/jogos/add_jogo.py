import streamlit as st
import pandas as pd
from pages.jogos import cria_csv
from pages.pagina_teste import pagina_teste

# file_path = "data/cvs/Jogos.csv"

def add_jogo():
  worksheet = pagina_teste.teste()
  return worksheet

  # last_row = df.shape[0]
  # st.write(last_row)
worksheet = add_jogo()
# st.write(worksheet)

# Function to find the last filled row in the worksheet.
def find_last_filled_row(worksheet):
    return len(worksheet.get_all_values()) + 1
  
# last = find_last_filled_row(worksheet)
# st.write(last)

  # values = df.values.tolist()
  # st.write(values)

# Function to insert data into the Google Sheet after the last filled row.
def insert_data_into_sheet(dataframe):
    worksheet = sheet.get_worksheet(0)  # Replace 0 with the index of your desired worksheet
    values = dataframe.values.tolist()  

    # Find the last filled row
    last_filled_row = find_last_filled_row(worksheet)

    # Insert the data after the last filled row
    worksheet.insert_rows(values, last_filled_row)

# # Your DataFrame with data to be inserted
# df = pd.DataFrame(results, columns=['query', 'batch_index', 'index_of_audio_output_tensor', 'audio_file_name', 'similarity_score_by_model', 'user_relevance_score'])

#----------------------
# if st.button("Carregar CSV"):
#         df = cria_csv.read_csv(file_path)
#         st.write("DataFrame Atual:")
#         st.write(df)

odd = st.number_input('Digite a Odd', key='odd')
responsabilidade = st.number_input('Digite a responsabilidade',key='responsabilidade')
lucro = st.number_input('Digite a lucro',key='lucro')
porcentagem = st.number_input('Digite a porcentagem',key='porcentagem')
odd_equivalente = st.number_input('Digite a odd_equivalente',key='odd_equivalente')
green = st.number_input('Digite a green',key='green')

nova_linha = pd.DataFrame({'odd': [odd], 'responsabilidade': [responsabilidade], 'lucro': [lucro], 'porcentagem': [porcentagem], 'odd_equivalente': [odd_equivalente], 'green': [green]})

if st.button("Adicionar Linhas"):
  # Call the function to insert data into the Google Sheet
  insert_data_into_sheet(nova_linha)
        # df_novo = pd.concat([df, nova_linha], ignore_index=True)
        # st.write("DataFrame Atualizado:")
        # st.write(df_novo)
        # df_novo.to_csv(file_path, index=False)
  st.success("Linhas adicionadas com sucesso!")
