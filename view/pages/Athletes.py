import streamlit as st
import pandas as pd

from styles.global_styles import applyGlobalStyles
from components.link import DefaultLink, GoBackLink as GoBackButton
from components.loading import Loading
from utils.sidebar import DefaultSidebar as Sidebar

def renderComponents():
    applyGlobalStyles()
    group = st.query_params.group
    GoBackButton(st, '/')
    Sidebar(st)
    Loading(st, 0.9)

def render():
    renderComponents()
    st.title('Atletas')
    df = pd.read_csv('https://raw.githubusercontent.com/LuannMateus/my-dataframes/main/athletics.csv')
    group = st.query_params.group
    athletes = df.loc[df['Grupo'] == group]
    for athlete in athletes['Nome'].unique():
        DefaultLink(st, f'/IndividualAnalysis?group={group}&name={athlete}', athlete)

render()
