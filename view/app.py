import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Application imports
from styles.global_styles import applyGlobalStyles
from components.link import DefaultLink as Link
from components.loading import Loading
from utils.sidebar import DefaultSidebar as Sidebar

def renderComponents():
    st.set_page_config(page_title='Inicío', layout='centered')
    applyGlobalStyles()
    Sidebar(st)
    Loading(st, 1)

def renderGraphics(df):
    # Gráfico de Pizza para Distribuição dos Grupos de Atletas
    group_counts = df['Grupo'].value_counts().reset_index()
    group_counts.columns = ['Grupo', 'Contagem']
    fig = px.pie(group_counts, names='Grupo', values='Contagem', title='Distribuição dos Grupos de Atletas')
    st.plotly_chart(fig)

    # Criar um gráfico de barras para a média de PSR por grupo
    avg_psr_por_group = df.groupby('Grupo')['PSR'].mean().reset_index()
    fig2 = px.bar(avg_psr_por_group, x='Grupo', y='PSR', title='Média de PSR por Grupo', labels={'PSR': 'Média de PSR'})
    st.plotly_chart(fig2)

    # Criar um gráfico de dispersão para PSE vs Carga de Treino
    fig3 = px.scatter(df, x='PSE', y='CargaDeTreino', title='Dispersão: PSE vs Carga de Treino', labels={'PSE': 'PSE', 'CargaDeTreino': 'Carga de Treino'})
    st.plotly_chart(fig3)

    # Criar um gráfico de linha para a evolução da média de PSR ao longo do tempo
    df['Data'] = pd.to_datetime(df['Data'])
    avg_psr_per_date = df.groupby('Data')['PSR'].mean().reset_index()
    fig4 = px.line(avg_psr_per_date, x='Data', y='PSR', title='Evolução da Média de PSR ao Longo do Tempo', labels={'Data': 'Data', 'PSR': 'Média de PSR'})
    st.plotly_chart(fig4)

def render():
    renderComponents()
    st.title('Big Data Atletas')
    df = pd.read_csv('https://raw.githubusercontent.com/LuannMateus/my-dataframes/main/athletics.csv')
    graphics_tab, categories_tab, info_tab = st.tabs(['Gráficos dos grupos', 'Grupos', 'Informações'])
    with graphics_tab:
        renderGraphics(df)
    with categories_tab:
        for group in df['Grupo'].unique():
            Link(st, f'/Athletes?group={group}', group)
    with info_tab:
        st.markdown('''
            ### Projeto: Painel de Visualização de Atletas

            #### Descrição do Projeto
            Este projeto consiste em um painel interativo desenvolvido com o Streamlit, que exibe dados de atletas de diferentes grupos etários, como Sub 19, Sub 17 e Sub 15. O painel fornece gráficos e visualizações detalhadas sobre o desempenho dos atletas, além de permitir a navegação entre diferentes grupos e detalhes individuais.

            #### Funcionalidades

            1. **Visualização de Dados por Grupos de Atletas**
            - Os dados dos atletas são exibidos de forma organizada, agrupados por categorias de idade, como Sub 19, Sub 17 e Sub 15.
            - Cada grupo tem seu próprio link navegável, permitindo que os usuários vejam os detalhes específicos de cada grupo.

            2. **Gráficos Diversificados**
            - Utilizando pandas e matplotlib, o projeto gera diversos gráficos para cada grupo e atleta individual.
            - Os gráficos incluem visualizações de PSR (Percepção Subjetiva de Recuperação), PSE (Percepção Subjetiva de Esforço) e Carga de Treino ao longo do tempo.
            - Cada gráfico é acompanhado por uma explicação detalhada, facilitando a compreensão dos dados apresentados.

            3. **Links Navegáveis**
            - Os links para os grupos de atletas são estilizados com CSS para uma aparência profissional, usando cores como azul e vermelho.
            - Um efeito zebrado é aplicado aos links para melhorar a legibilidade e a navegação visual.
            - Os links são apresentados dentro de um container estilizado, que possui um fundo cinza claro, e uma sombra sutil para profundidade.

            4. **Botão Flutuante para Navegação**
            - Um botão flutuante estilizado com CSS é adicionado para permitir que os usuários voltem à página anterior.
            - O botão é fixado no canto direito da tela e possui transições suaves de cor, garantindo uma navegação intuitiva e agradável.

            #### Estilo e Design
            O design do painel foi pensado para ser visualmente atraente e funcional. A utilização de cores vibrantes como vermelho e azul, combinada com efeitos de transição e sombras sutis, cria uma experiência de usuário envolvente. Os elementos são organizados de forma clara, com atenção aos detalhes, como espaçamentos, bordas arredondadas e efeitos de hover.
        ''')

render()
