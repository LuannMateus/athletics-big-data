import streamlit as st
from app import App

st.set_page_config(initial_sidebar_state="collapsed")
no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)

def app():
    app = App()
    app.addPage('Page One', home.app)
    app.addPage('Page Two', detail.app)
    st.title('APP2')
    st.write('Welcome to app2')
    queryParams = st.query_params
    st.write(queryParams)

app()
