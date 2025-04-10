import os
import openai

class GeneradorResumen:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def generar(self, texto):
        respuesta = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Resume el siguiente contenido para investigación."},
                {"role": "user", "content": texto}
            ],
            temperature=0.5,
            max_tokens=400
        )
        return respuesta.choices[0].message.content