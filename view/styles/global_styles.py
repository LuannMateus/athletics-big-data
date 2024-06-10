import streamlit as st


def applyGlobalStyles():
    st.markdown(
        f'''
            <style>
                #tabs-bui3-tabpanel-1 > div > div > div p:nth-child(even),
                #tabs-bui3-tabpanel-1 > div > div > div p:nth-child(even),
                #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div.st-emotion-cache-0.e1f1d6gn0 > div > div p:nth-child(even),
                .st-emotion-cache-1n76uvr .e1f1d6gn2 p:nth-child(even) {{
                    background-color: #e74c3c;
                    padding: 12px;
                }}
                
                #tabs-bui2-tabpanel-0 > div > div > div {{
                    background-color: transparent !important;
                }}
                
                #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1itdyc2.eczjsme11 > div.st-emotion-cache-6qob1r.eczjsme3 > div.st-emotion-cache-79elbk.eczjsme10 > ul {{
                    display: none;
                }}
            </style>
        ''',
        unsafe_allow_html=True
    )
