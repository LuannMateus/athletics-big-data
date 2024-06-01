import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from styles.global_styles import applyGlobalStyles
from components.link import DefaultLink as Link
from utils.sidebar import DefaultSidebar as Sidebar

def renderComponents():
    applyGlobalStyles()
    Sidebar(st)

def renderGraphics(df):
    # Criar um gráfico de barras para a média de PSR por grupo
    st.write("Gráfico de barras para a média de PSR por grupo:")
    media_psr_por_grupo = df.groupby("Grupo")["PSR"].mean()
    fig1, ax1 = plt.subplots()
    media_psr_por_grupo.plot(kind="bar", ax=ax1)
    plt.xlabel("Grupo")
    plt.ylabel("Média de PSR")
    st.pyplot(fig1)

    # Criar um gráfico de dispersão para PSE vs Carga de Treino
    st.write("Gráfico de dispersão para PSE vs Carga de Treino:")
    fig2, ax2 = plt.subplots()
    df.plot.scatter(x="PSE", y="CargaDeTreino", ax=ax2)
    plt.xlabel("PSE")
    plt.ylabel("Carga de Treino")
    st.pyplot(fig2)

    # Criar um gráfico de linha para a evolução da média de PSR ao longo do tempo
    st.write("Gráfico de linha para a evolução da média de PSR ao longo do tempo:")
    df["Data"] = pd.to_datetime(df["Data"])
    media_psr_por_data = df.groupby("Data")["PSR"].mean()
    fig3, ax3 = plt.subplots()
    media_psr_por_data.plot(ax=ax3)
    plt.xlabel("Data")
    plt.ylabel("Média de PSR")
    st.pyplot(fig3)

def render():
    renderComponents()
    st.title('Big Data Atletas')
    df = pd.read_csv('https://raw.githubusercontent.com/LuannMateus/my-dataframes/main/bigdataathleticsmock.csv')
    graphicsTab, categoriesTab = st.tabs(["Gráficos dos grupos", "Grupos",])
    with graphicsTab:
        renderGraphics(df)
    with categoriesTab:
        for group in df['Grupo'].unique():
            Link(st, f"http://192.168.0.10:8501/Athletes?group={group}", group)

render()
