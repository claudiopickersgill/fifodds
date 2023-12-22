import streamlit as st
from pages.jogos import cria_csv


def principal():
    st.title('Alooo, Fifih!!!')
    st.write('Usa o Menu do lado pra navegar entre as diferentes fases do projeto')
    st.write('Vou deixar de brinde essa imagem que encontrei nos confins do meu HD')
    st.image('data/img/odds.png')

    file_path = "data/cvs/Jogos.csv"
    if st.button("Carregar CSV"):
        df = cria_csv.read_csv(file_path)
        st.write("DataFrame Atual:")
        st.write(df)
