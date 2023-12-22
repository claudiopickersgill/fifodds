import streamlit as st

def odds():
    st.title('Aloouuu... vamos calcular a porcetagem em cima da Odd da aposta!!')
    st.write(
        'Digite o valor da Odd que deseja calcular a porcentagem:')
    odd = st.number_input('Digite seu número:')
    st.write(
        'Vamos calcular o percentual com base em um lucro de R$100,00')
    lucro = 100
    responsabilidade = (odd - 1) * lucro
    st.write('Para ter um lucro de R$100,00...')
    st.write('Precisaremos apostar (responsabilidade) um total de:',round(responsabilidade))
    st.write('O valor da Responsabilidade está arredondado!!!')
    st.write('Agora, vamos ver a porcetagem de lucro, baseado no valor investido (responsabilidade), lucro, e Odds:')
    porcentagem = (lucro * 100) / responsabilidade
    st.write(f'De acordo com os dados disponíveis, temos uma porcentagem de lucro igual a: {porcentagem} %')