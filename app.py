import streamlit as st
from dotenv import load_dotenv
from modulos.buscador import BuscadorWeb
from modulos.resumen import GeneradorResumen
from modulos.visualizador import VisualizadorContenido

load_dotenv()

st.set_page_config(page_title="Asistente de Investigación Digital")
st.title("🧠 Asistente de Investigación Digital")
tema = st.text_input("🔍 Ingresa el tema a investigar:")

if tema:
    with st.spinner("Buscando información..."):
        buscador = BuscadorWeb()
        resultados = buscador.buscar(tema)
        st.success("Búsqueda completada")

    with st.expander("🌐 Resultados encontrados"):
        VisualizadorContenido.mostrar_resultados(resultados)

    with st.spinner("Resumiendo contenido..."):
        generador = GeneradorResumen()
        resumen = generador.generar(resultados)
        st.subheader("📝 Resumen")
        st.write(resumen)

    with st.spinner("Generando nube de palabras..."):
        VisualizadorContenido.generar_nube(resultados)
