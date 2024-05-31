import streamlit as st

from app import App

def app():
    app = App()
    app.addPage('Page One', home.app)
    app.addPage('Page Two', detail.app)
    st.markdown('<a href="http://172.17.2.23:8501/detail" target="_self">Next page</a>', unsafe_allow_html=True)

