import streamlit as st
import pandas as pd
from pages.jogos import cria_csv

def add_jogo():
    file_path = "data/cvs/Jogos.csv"
    if st.button("Recarregar CSV"):
        df = cria_csv.read_csv(file_path)
        st.write("DataFrame Atual:")
        st.write(df)

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
