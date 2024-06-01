import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Application imports
from styles.global_styles import applyGlobalStyles
from components.link import DefaultLink as Link
from components.loading import Loading
from utils.sidebar import DefaultSidebar as Sidebar

def renderComponents():
    applyGlobalStyles()
    Sidebar(st)
    Loading(st, 1)

def renderGraphics(df):
    # Gráfico de Pizza para Distribuição dos Grupos de Atletas
    st.write('Gráfico de pizza para a distribuição dos grupos de atletas:')
    group_counts = df['Grupo'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(group_counts, labels=group_counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Mantém o aspecto de um círculo
    plt.title('Distribuição dos Grupos de Atletas')
    st.pyplot(fig)
            
    # Criar um gráfico de barras para a média de PSR por grupo
    st.write('Gráfico de barras para a média de PSR por grupo:')
    avg_psr_por_group = df.groupby('Grupo')['PSR'].mean()
    fig1, ax1 = plt.subplots()
    avg_psr_por_group.plot(kind='bar', ax=ax1)
    plt.xlabel('Grupo')
    plt.ylabel('Média de PSR')
    st.pyplot(fig1)

    # Criar um gráfico de dispersão para PSE vs Carga de Treino
    st.write('Gráfico de dispersão para PSE vs Carga de Treino:')
    fig2, ax2 = plt.subplots()
    df.plot.scatter(x='PSE', y='CargaDeTreino', ax=ax2)
    plt.xlabel('PSE')
    plt.ylabel('Carga de Treino')
    st.pyplot(fig2)

    # Criar um gráfico de linha para a evolução da média de PSR ao longo do tempo
    st.write('Gráfico de linha para a evolução da média de PSR ao longo do tempo:')
    df['Data'] = pd.to_datetime(df['Data'])
    avg_psr_per_date = df.groupby('Data')['PSR'].mean()
    fig3, ax3 = plt.subplots()
    avg_psr_per_date.plot(ax=ax3)
    plt.xlabel('Data')
    plt.ylabel('Média de PSR')
    st.pyplot(fig3)

def render():
    renderComponents()
    st.title('Big Data Atletas')
    df = pd.read_csv('https://raw.githubusercontent.com/LuannMateus/my-dataframes/main/bigdataathleticsmock.csv')
    graphics_tab, categories_tab, info_tab = st.tabs(['Gráficos dos grupos', 'Grupos', 'Informações'])
    with graphics_tab:
        renderGraphics(df)
    with categories_tab:
        for group in df['Grupo'].unique():
            Link(st, f'http://192.168.0.10:8501/Athletes?group={group}', group)
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
