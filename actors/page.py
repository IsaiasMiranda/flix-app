from datetime import datetime

import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

from actors.service import ActorService


def show_actors():
    actor_service = ActorService()
    actors = actor_service.get_actors()

    if actors:
        st.write('Lista de Atores:')
        actors_df = pd.json_normalize(actors)
        AgGrid(
            data=actors_df,
            reload_data=True,
            key='actors_grid'
        )
    else:
        st.warning('Nenhum Ator/Atriz cadastrado!')

    st.title('Cadastrar novo Ator/Atriz')

    name = st.text_input('Nome do Ator/Atriz')
    birthday = st.date_input('Data de Nascimento')
    nationality = st.text_input('Nacionalidade')

    new_actor_data = {
        'name': name,
        'birthday': datetime.strptime(birthday, '%Y-%m-%d'),
        'nationality': nationality,
    }
    if st.button('Cadastrar'):
        new_actor = actor_service.create_actor(new_actor_data)
        st.success(f'Ator/Atriz: "{name}" cadastrado com sucesso!')
