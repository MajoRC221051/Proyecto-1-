import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re

class VisualizadorContenido:

    @staticmethod
    def mostrar_resultados(texto):
        st.write(texto)

    @staticmethod
    def generar_nube(texto):
        texto_filtrado = re.sub(r'[^\w\s]', '', texto.lower())
        nube = WordCloud(width=800, height=400, background_color='white').generate(texto_filtrado)
        plt.figure(figsize=(10, 5))
        plt.imshow(nube, interpolation='bilinear')
        plt.axis("off")
        st.pyplot(plt)
