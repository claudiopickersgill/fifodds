import streamlit as st
import pandas as pd
from pages.conexao import conexao


def cria_df():
    worksheet = conexao.faz_conexao()
    dataframe = pd.DataFrame(worksheet.get_all_records())

    return dataframe
