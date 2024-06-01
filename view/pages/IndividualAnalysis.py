import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from components.link import GoBackLink as GoBackButton
from components.loading import Loading
from utils.sidebar import DefaultSidebar as Sidebar

def renderComponents():
    GoBackButton(st)
    Sidebar(st)
    Loading(st, 0.9)

def renderGraphics(df, athleteName):
    # Gráfico de linha para a evolução do PSR ao longo do tempo
    st.write(f'Gráfico para a evolução do PSR:')
    fig1, ax1 = plt.subplots()
    df.plot(x='Data', y='PSR', ax=ax1)
    plt.xlabel('Data')
    plt.ylabel('PSR')
    plt.title(f'Evolução do PSR para {athleteName}')
    st.pyplot(fig1)

    # Gráfico de linha para a evolução do PSE ao longo do tempo
    st.write(f'Gráfico para a evolução do PSE:')
    fig2, ax2 = plt.subplots()
    df.plot(x='Data', y='PSE', ax=ax2)
    plt.xlabel('Data')
    plt.ylabel('PSE')
    plt.title(f'Evolução do PSE para {athleteName}')
    st.pyplot(fig2)

    # Gráfico de linha para a evolução da Carga de Treino ao longo do tempo
    st.write(f'Gráfico para a evolução da Carga de Treino:')
    fig3, ax3 = plt.subplots()
    df.plot(x='Data', y='CargaDeTreino', ax=ax3)
    plt.xlabel('Data')
    plt.ylabel('Carga de Treino')
    plt.title(f'Evolução da Carga de Treino para {athleteName}')
    st.pyplot(fig3)

def render():
    renderComponents()
    df = pd.read_csv('https://raw.githubusercontent.com/LuannMateus/my-dataframes/main/bigdataathleticsmock.csv')
    athlete_name = st.query_params.name
    st.title(f'Gráficos de {athlete_name}')
    athlete_df = df.loc[df['Nome'] == athlete_name]
    renderGraphics(athlete_df, athlete_name)

render()
