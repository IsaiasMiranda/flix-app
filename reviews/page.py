import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


reviews = [
    {
        'id': 1,
        'stars': 5
    },
    {
        'id': 2,
        'stars': 3
    },
    {
        'id': 3,
        'stars': 4
    }
]


def show_reviews():
    st.write('Lista de Filmes:')

    AgGrid(
        data=pd.DataFrame(reviews),
        reload_data=True,
        key='reviews_grid'
    )

    st.title('Cadastrar novo Gênero')
    name = st.text_input('Nome do Gênero')
    if st.button('Cadastrar'):
        st.success(f'Gênero "{name}" cadastrado com sucesso!')
