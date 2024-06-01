def GoBackButton(st, label, onClick):
    st.(label, on_click=onClick)
    st.markdown(
        """
        <style>
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div:nth-child(1) > div > button {
                position: fixed;
                right: 20px;
                background-color: #f63366;
                color: white;
                padding: 10px 20px;
                border-radius: 5px;
                font-size: 16px;
                cursor: pointer;
                z-index: 1000;
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
            }
            .floating-button:hover {
                background-color: #f9527e;
            }
        </style>
        """
        , unsafe_allow_html=True
    )
