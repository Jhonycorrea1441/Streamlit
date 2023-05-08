import streamlit as st
from Global import Global_pages
from Movilidad import Movilidad_pages
from Uber import Uber_pages

# Configuración de la barra lateral
st.sidebar.title('Menú')
pages = {
    'Inicio': Global_pages,
    'Acerca de': Movilidad_pages,
    'Contacto': Uber_pages,
}

# Renderizado de la página seleccionada en la barra lateral
selection = st.sidebar.radio('Navegar', list(pages.keys()))
page = pages[selection]
page()