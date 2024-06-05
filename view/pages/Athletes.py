import streamlit as st
import pandas as pd

from styles.global_styles import applyGlobalStyles
from components.link import DefaultLink, GoBackLink as GoBackButton
from components.loading import Loading
from utils.sidebar import DefaultSidebar as Sidebar

def renderComponents():
    st.set_page_config(page_title=f'Atletas | {st.query_params.group}', layout='centered')
    applyGlobalStyles()
    GoBackButton(st, '/~/+')
    Sidebar(st)
    Loading(st, 0.9)

def render():
    renderComponents()
    st.title('Atletas')
    df = pd.read_csv('https://raw.githubusercontent.com/LuannMateus/my-dataframes/main/athletics.csv')
    group = st.query_params.group
    athletes = df.loc[df['Grupo'] == group]
    st.write("")
    with st.container():
        for athlete in athletes['Nome'].unique():
            DefaultLink(st, f'/IndividualAnalysis?group={group}&name={athlete}', athlete)

render()
