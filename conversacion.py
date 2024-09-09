import random

def obtener_respuesta(pregunta, respuestas):
    """ Devuelve una respuesta aleatoria para una pregunta dada. """
    if pregunta in respuestas:
        return random.choice(respuestas[pregunta])
    else:
        return "Lo siento, no entiendo la pregunta."

def main():
    # Diccionario con preguntas y respuestas
   
    respuestas = {
    "¿Cómo estás?": ["¡Estoy bien, gracias!", "¡Genial! ¿Y tú?", "¡Estoy aquí para ayudarte!"],
    "¿Cuál es tu nombre?": ["Mi nombre es Luzi.", "Me llamo Luzi, ¿y tú?", "Soy Luzi, tu asistente."],
    "¿Qué puedes hacer?": ["Puedo responder a preguntas básicas.", "Estoy aquí para ayudarte con información simple.", "Puedo mantener una conversación básica contigo."],
    "¿Cuál es tu color favorito?": ["No tengo un color favorito, pero me gustan todos los colores.", "No tengo preferencias en colores.", "¡Los colores son geniales en general!"],
    # Agrega nuevas preguntas y respuestas aquí
    "¿Cuál es tu comida favorita?": ["Me encanta la pizza.", "No tengo una comida favorita, pero disfruto muchas cosas.", "La comida es deliciosa en general."],
    "¿De dónde eres?": ["Soy un programa creado por Fernando.", "Mexico"],
    "que haces":["nada y tu","viendo LOL"]

}

    
    print("Hola, soy Luzi. ¿En qué puedo ayudarte hoy?")
    
    while True:
        pregunta = input("Tú: ")
        if pregunta.lower() in ['salir', 'adiós', 'chau']:
            print("Luzi: ¡Hasta luego!")
            break
        respuesta = obtener_respuesta(pregunta, respuestas)
        print("Luzi:", respuesta)

if __name__ == "__main__":
    main()
