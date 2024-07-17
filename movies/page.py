import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


movies = [
    {
        'id': 1,
        'name': 'Os Mercenários'
    },
    {
        'id': 2,
        'name': 'Evil Dead, A morte do Demônio'
    },
    {
        'id': 3,
        'name': 'Um tira da Pesada 4'
    }
]


def show_movies():
    st.write('Lista de Filmes:')

    AgGrid(
        data=pd.DataFrame(movies),
        reload_data=True,
        key='movies_grid'
    )

    st.title('Cadastrar novo Gênero')
    name = st.text_input('Nome do Gênero')
    if st.button('Cadastrar'):
        st.success(f'Gênero "{name}" cadastrado com sucesso!')
