def DefaultSidebar(st):
    with st.sidebar:
        st.page_link(label = 'Inicío', page = 'app.py')

    no_sidebar_style = """
        <style>
            .st-emotion-cache-1s0bj5q {
                padding-top: 2rem !important;
            }

            ul [data-testid="stSidebarNavItems" class="st-emotion-cache-1s0bj5q eczjsme9"] {
                display: none;
            }

            button[data-testid="baseButton-header"] {
                display: none !important;
            }

            #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1itdyc2.eczjsme11 > div.st-emotion-cache-6qob1r.eczjsme3 > div.st-emotion-cache-79elbk.eczjsme10 > ul > li:nth-child(1) > div > a {
                display: none;
            }

            #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1itdyc2.eczjsme11 > div.st-emotion-cache-6qob1r.eczjsme3 > div.st-emotion-cache-79elbk.eczjsme10 > ul > li:nth-child(2) > div > a {
                display: none;
            }

            #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1itdyc2.eczjsme11 > div.st-emotion-cache-6qob1r.eczjsme3 > div.st-emotion-cache-79elbk.eczjsme10 > ul > li:nth-child(3) > div > a {
                display: none;
            }
        </style>
    """
    st.markdown(no_sidebar_style, unsafe_allow_html = True)
