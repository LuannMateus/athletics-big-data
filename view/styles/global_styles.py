import streamlit as st


def applyGlobalStyles():
    st.markdown(
        f'''
            <style>
                #tabs-bui3-tabpanel-1 > div > div > div p:nth-child(even),
                #tabs-bui3-tabpanel-1 > div > div > div p:nth-child(even),
                #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div.st-emotion-cache-0.e1f1d6gn0 > div > div p:nth-child(even),
                .e1f1d6gn2 > p:nth-child(even),
                .e1f1d6gn2 p:nth-child(even) {{
                    background-color: #e74c3c;
                    padding: 12px;
                }}
                
                #tabs-bui2-tabpanel-0 > div > div > div {{
                    background-color: transparent !important;
                }}
            </style>
        ''',
        unsafe_allow_html=True
    )
