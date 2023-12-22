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
    st.write('Precisaremos apostar um total de R$:',round(responsabilidade))
    st.write('OBS: O valor da Responsabilidade está arredondado!!!')    
    st.write('Para obter um Lucro de R$:',lucro)
    st.write('----------------------------------------------------')
    st.write('Vamos calcular o Percentual com base em um Lucro de R$:',lucro)    
    st.write(f'Agora, vamos ver a porcetagem de Lucro, baseado no na Responsabilidade de R$:{responsabilidade}, no Lucro de R$:{lucro}, e na Odd de {odd}:')
    porcentagem = (lucro * 100) / responsabilidade
    st.write(f'De acordo com os dados disponíveis, temos uma porcentagem de Lucro igual a: {porcentagem} %')
