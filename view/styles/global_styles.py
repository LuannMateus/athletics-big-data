import streamlit as st


def applyGlobalStyles():
    st.markdown(
        f'''
            <style>
                #tabs-bui2-tabpanel-1 > div > div > div,
                #tabs-bui2-tabpanel-0 > div > div > div {{
                    background-color: #f8f9fa;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); 
                    border-radius: 0;
                }}

                #tabs-bui2-tabpanel-1 > div > div > div p:nth-child(even),
                #tabs-bui2-tabpanel-0 > div > div > div p:nth-child(even) {{
                    background-color: #e74c3c; /* Darker grey for even rows */
                    padding: 12px;
                }}
            </style>
        ''',
        unsafe_allow_html=True
    )
