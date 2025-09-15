import streamlit as st
import pandas as pd

st.sidebar.image("logo.png")
st.sidebar.title("Canadian Artists")

artistas = ['Josh Beauchamp', 'Shawn Mendes', 'Justin Bieber']

opcao = st.sidebar.selectbox('Escolha o Artista.', artistas )

st.title('Canadian Artists')

st.image(f'{opcao}.png')
st.markdown(f'Artista: {opcao}')
st.markdown('---')

if opcao == 'Josh Beauchamp':
    st.write('Josh Beauchamp, nascido em 31 de março de 2000 em St. Albert, Canadá, é dançarino, cantor e coreógrafo. Começou a dançar aos 6 anos e se destacou em estúdios como o immaBEAST e em programas como World of Dance. Ganhou fama mundial como integrante e capitão de dança do grupo pop global Now United, onde representou o Canadá de 2017 a 2022. Após sua saída, iniciou sua carreira solo na música, explorando novos projetos como artista solo.')

elif opcao == 'Shawn Mendes':
    st.write('Shawn Mendes (Shawn Peter Raul Mendes), nascido em 8 de agosto de 1998 em Pickering, Ontário, Canadá, é um cantor, compositor e músico. Ele ganhou fama inicialmente postando vídeos de covers no Vine em 2013, o que rapidamente chamou a atenção do público e da indústria musical. Seu álbum de estreia, Handwritten (2015), teve grande sucesso, com hits como "Stitches". Desde então, Shawn lançou vários álbuns de sucesso, incluindo Illuminate (2016) e Shawn Mendes (2018), consolidando-se como um dos principais nomes do pop mundial.')

elif opcao == 'Justin Bieber':
    st.write('Justin Bieber, nascido em 1º de março de 1994 em London, Ontário, Canadá, é cantor, compositor e ator. Descoberto em 2008 após postar vídeos no YouTube, rapidamente alcançou fama mundial com seu single "One Time" e o álbum My World (2009). Tornou-se um ícone pop com sucessos como "Baby", "Sorry" e "Love Yourself". Ao longo da carreira, passou por transformações musicais e pessoais. Justin também é pai, fato que trouxe ainda mais maturidade à sua vida e música.')
    