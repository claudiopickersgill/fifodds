import streamlit as st

def odds():
    st.title('Aloouuu... vamos calcular a porcetagem em cima da Odd da aposta!!')
    st.write(
        'Digite o valor da Odd que deseja calcular a porcentagem:')
    odd = st.number_input('Digite a ODD:')
    st.write(f'Você está calculando a porcentagem da Odd: {odd}')
    st.write('----------------------------------------------------')
    lucro = 100
    responsabilidade = (odd - 1) * lucro
    st.write('Precisaremos apostar (responsabilidade) um total de: ',round(responsabilidade))
    st.write('OBS: O valor da Responsabilidade está arredondado!!!')    
    st.write(f'Para obter um lucro de R${lucro}')
    st.write('\n')
    st.write('Vamos calcular o percentual com base em um lucro de R$100,00')    
    st.write(f'Agora, vamos ver a porcetagem de lucro, baseado no na responsabilidade de {responsabilidade}, no lucro de {lucro}, e na Odd de {odd}:')
    porcentagem = (lucro * 100) / responsabilidade
    st.write(f'De acordo com os dados disponíveis, temos uma porcentagem de lucro igual a: {porcentagem} %')
