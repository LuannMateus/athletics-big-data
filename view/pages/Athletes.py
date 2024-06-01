import streamlit as st
import pandas as pd

from components.link import DefaultLink, GoBackLink as GoBackButton
from utils.sidebar import DefaultSidebar as Sidebar

def renderComponents():
    GoBackButton(st)
    Sidebar(st)

def render():
    renderComponents()
    st.title('Atletas')
    df = pd.read_csv('https://raw.githubusercontent.com/LuannMateus/my-dataframes/main/bigdataathleticsmock.csv')
    group = st.query_params.group
    athletes = df.loc[df['Grupo'] == group]
    for athlete in athletes['Nome']:
        DefaultLink(st, f"http://192.168.0.10:8501/IndividualAnalysis?group={group}&name={athlete}", athlete)

render()
