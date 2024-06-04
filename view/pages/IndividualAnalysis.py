import streamlit as st
import pandas as pd
import plotly.express as px

from components.link import GoBackLink as GoBackButton
from components.loading import Loading
from utils.sidebar import DefaultSidebar as Sidebar

def renderComponents():
    st.set_page_config(page_title=f'Análise | {st.query_params.name}', layout='centered')
    GoBackButton(st, f'/Athletes?group={st.query_params.group}')
    Sidebar(st)
    Loading(st, 0.9)

def renderGraphics(df, athleteName):
    # Gráfico de linha para risco de lesão
    df['RiscoLesao'] = df['PSR'] * df['PSE'] * df['CargaDeTreino'] / 1000  # Exemplo de cálculo
    fig_risco = px.line(df, x='Data', y='RiscoLesao', title=f'Evolução do Risco de Lesão para {athleteName}', labels={'Data': 'Data', 'RiscoLesao': 'Risco de Lesão'})
    st.plotly_chart(fig_risco)
    
    # Gráfico de linha para a evolução do PSR ao longo do tempo
    fig1 = px.line(df, x='Data', y='PSR', title=f'Evolução do PSR para {athleteName}', labels={'Data': 'Data', 'PSR': 'PSR'})
    st.plotly_chart(fig1)

    # Gráfico de linha para a evolução do PSE ao longo do tempo
    fig2 = px.line(df, x='Data', y='PSE', title=f'Evolução do PSE para {athleteName}', labels={'Data': 'Data', 'PSE': 'PSE'})
    st.plotly_chart(fig2)

    # Gráfico de linha para a evolução da Carga de Treino ao longo do tempo
    fig3 = px.line(df, x='Data', y='CargaDeTreino', title=f'Evolução da Carga de Treino para {athleteName}', labels={'Data': 'Data', 'CargaDeTreino': 'Carga de Treino'})
    st.plotly_chart(fig3)

def render():
    renderComponents()
    df = pd.read_csv('https://raw.githubusercontent.com/LuannMateus/my-dataframes/main/athletics.csv')
    athlete_name = st.query_params.name
    st.title(f'Gráficos de {athlete_name}')
    athlete_df = df.loc[df['Nome'] == athlete_name]
    renderGraphics(athlete_df, athlete_name)

render()
