# Proyecto-1-

# Asistente de Investigación Digital Interactivo

## Descripción

Este proyecto consiste en el desarrollo de una aplicación web interactiva que funciona como un asistente de investigación digital. La herramienta permite al usuario ingresar un tema de interés y realiza una búsqueda automática de información actualizada en la web mediante la API de Tavily. Luego, analiza el contenido encontrado utilizando modelos de lenguaje natural de OpenAI a través de LangChain, generando un resumen automático y una visualización interactiva (nube de palabras) de las palabras más frecuentes.

La aplicación está desarrollada con Streamlit para ofrecer una interfaz amigable y dinámica.

---

## Características principales

- Entrada de tema de interés por parte del usuario.
- Uso de un agente ReAct de LangChain para búsqueda mediante la API de Tavily.
- Visualización de resultados de búsqueda con título, extracto y enlace.
- Resumen automático del contenido encontrado utilizando OpenAI GPT-4 mini.
- Generación de nube de palabras (WordCloud) basada en el texto recopilado.
- Interfaz modularizada con código separado en carpeta `/modulos`.
- Uso de archivo `.env` para protección de claves API (las claves no están incluidas en el repositorio).

---

## Estructura del proyecto

