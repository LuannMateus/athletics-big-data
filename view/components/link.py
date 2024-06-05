def DefaultLink(st, href, label):
    return st.markdown(f'''
            <style>
                .custom-link {{                    
                    color: #ffffff !important;
                    font-weight: 600;
                    text-decoration: none;
                    padding: 8px 12px;
                    border-radius: 5px;
                    transition: background-color 0.3s ease, color 0.3s ease;
                }}
            </style>
            <a class="custom-link" href="{href}" target="_self">{label}</a>
        ''',
        unsafe_allow_html=True
    )

def GoBackLink(st, path):
    return st.markdown(
        f'''
        <style>
            .go-back-link {{
                position: fixed;
                right: 20px;
                background-color: #f63366;
                color: white !important;
                padding: 10px 20px;
                border-radius: 5px;
                font-size: 16px;
                cursor: pointer;
                z-index: 1000;
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
                text-decoration: none;
                text-align: center;
            }}

            .go-back-link:hover {{
                background-color: #f9527e;
            }}
        </style>
        <a class="go-back-link" href="{path}" target="_parent">Voltar</a>
        '''
        , unsafe_allow_html=True
    )
