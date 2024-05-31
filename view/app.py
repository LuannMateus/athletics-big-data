import streamlit as st

# Remove pages sidebar
st.set_page_config(initial_sidebar_state="collapsed")
no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)

import pages.detail as detail
import pages.home as home

class App:
    def __init__(self):
        self.pages = []

    def addPage(self, title, function):
        self.pages.append({
            "title": title,
            "function": function
        })

    def run(self):
        page = st.sidebar.selectbox(
            'Navegação',
            self.pages,
            format_func= lambda page: page['title']
        )
        page['function']()

def main():
    app = App()
    st.title('Athletics Big Data')
    app.addPage('Page One', home.app)
    app.addPage('Page Two', detail.app)
    # st.markdown('<a href="http://172.17.2.23:8501/detail" target="_self">Next page</a>', unsafe_allow_html=True)
    app.run()

if __name__ == '__main__':
    main()
