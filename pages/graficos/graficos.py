import streamlit as st
import pandas as pd
from pages.conexao import cria_df
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set_style(rc={'axes.facecolor': '#0E1117',
                  'axes.edgecolor': 'white',
                  'axes.labelcolor': 'white',
                  'text.color': 'white',
                  'xtick.color': 'white',
                  'ytick.color': 'white',
                  'axes.grid': True,
                  'grid.color': '.6',
                  "grid.linestyle": ":"})
fundo = '#0E1117'
loc = 'upper right'


def graficos():
    df = cria_df.cria_df()

    grouped_data = df.groupby('green').size()
    fig, ax = plt.subplots(figsize=(6, 6))
    explode = (0, 0.05)
    plt.pie(grouped_data, explode=explode,
            autopct='%0.2f%%', startangle=270, colors=['red', 'blue'])
    ax.axis('equal')
    plt.legend(labels=grouped_data.index, facecolor=fundo, loc=loc)
    ax.set_title('Porcentagem de Vitórias', color='white')
    fig.patch.set_facecolor(fundo)

    st.pyplot(fig)

    st.title('------------------------------------------------')

    fig1, ax1 = plt.subplots(figsize=(6, 6))
    sns.histplot(df['odd'], bins=20, kde=True, color='blue')
    plt.title('Distribuição de Odds')
    fig1.patch.set_facecolor(fundo)

    st.pyplot(fig1)

    st.title('------------------------------------------------')

    fig2, ax2 = plt.subplots(figsize=(6, 6))
    sns.scatterplot(x='responsabilidade', y='lucro', hue='green',
                    data=df, palette={'sim': 'blue', 'nao': 'red'})
    plt.title('Relação entre Lucro e Responsabilidade')
    plt.legend(loc=loc)
    fig2.patch.set_facecolor(fundo)

    st.pyplot(fig2)

    st.title('------------------------------------------------')

    fig3, ax3 = plt.subplots(figsize=(6, 6))
    sns.scatterplot(x='odd', y='lucro', hue='green', data=df,
                    palette={'sim': 'blue', 'nao': 'red'})
    plt.title('Relação entre Odds e Lucro')
    plt.legend(loc=loc)
    fig3.patch.set_facecolor(fundo)

    st.pyplot(fig3)

    st.title('------------------------------------------------')

    fig4, ax4 = plt.subplots(figsize=(6, 6))
    sns.barplot(x='tipo_jogo', y='lucro', data=df, errorbar=None, hue='green',
                palette={'sim': 'blue', 'nao': 'red'}, legend=False)
    plt.title('Análise de Lucro por Categoria')
    fig4.patch.set_facecolor(fundo)

    st.pyplot(fig4)

    st.title('------------------------------------------------')

    desc_stats = df.describe()
    st.write(desc_stats)

    st.title('------------------------------------------------')

    fig5, ax5 = plt.subplots(figsize=(6, 6))
    sns.scatterplot(x='porcentagem', y='odd_equivalente', hue='green',
                    data=df, palette={'sim': 'blue', 'nao': 'red'})
    plt.title('Análise de Porcentagem e Odd Equivalente')
    plt.legend(loc=loc)
    fig5.patch.set_facecolor(fundo)

    st.pyplot(fig5)

    st.title('------------------------------------------------')

    fig6, ax6 = plt.subplots(figsize=(6, 6))
    sns.scatterplot(x='odd', y='odd_equivalente', hue='green',
                    data=df, palette={'sim': 'blue', 'nao': 'red'})
    plt.title('Análise de Porcentagem e Odd')
    plt.legend(loc=loc)
    fig6.patch.set_facecolor(fundo)

    st.pyplot(fig6)
