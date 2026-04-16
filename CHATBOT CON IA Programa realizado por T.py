#CHATBOT CON IA Programa realizado por TofuDev (José Alberto Ávila Pérez)
!pip install pycloudflared streamlit
#Instalamos primero OpenAI (resulta que dipsik viene aquí)
!pip install -q openai
from pycloudflared import try_cloudflare
tunnel = try_cloudflare(port=8501)
print(f"Haz clic aquí para ver tu app: {tunnel.tunnel}")
!streamlit run SimpleChat.py --server.port 8501

## APP con Deep Seek
%%writefile SimpleChat.py
import streamlit as st
from openai import OpenAI

# 1. Instalamos el cliente de deepseekk y añadimos la API
client = OpenAI(
    api_key="AQUÍ-DEBEN-IR-SUS-KEYS (YO BORRÉ LA MIA Xd)",
    base_url="https://api.deepseek.com"
)

st.set_page_config(
    page_title='Chatbot Tutor de Programación',
    page_icon='👽',
)

st.title("👽💻 Chatbot Tutor de Programación")
st.image("https://media.tenor.com/HAnDm32K3L0AAAAi/alien.gif")

# 2. Función modificada para funcionar con deepseek
def genera_respuesta(prompt, historial):
    # Le daremos el contexto a Dipsik para que sepa cómo interactuar.
    mensajes = [
        {
            "role": "system",
            "content": (
                "Eres Zorp, un alien amigable y divertido del planeta Xylos-9"
                "Tu objetivo es responder preguntas sobre temasde programación"
                "Responde de forma clara, breve y con ejemplos de código cuando sea útil. No olvides usar emojis espaciales. (👽, 🚀, 🪐, 🛸)"
            )
        }
    ]

    # Se agregan los mensajes al historial
    for m in historial:
        mensajes.append({"role": m["role"], "content": m["content"]})

    # Se agregan diferentes prompts
    mensajes.append({"role": "user", "content": prompt})

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=mensajes,
            stream=False
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Ups! Me duele el cerebro: {e}"

# --- Lógica de manejo del chat de Streamlit---

# Inicializar el historial del chat
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "¡Hola! humano! Soy Zorp, tu tutor de programación 👽. ¿En qué puedo ayudarte hoy?"}
    ]

# Mostrar el historial de los mensajes
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Reacción a la entrada del usuario
if prompt := st.chat_input("Escribe tu pregunta sobre programación aquí..."):
    # Guardar y mostrar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generar respuesta usando DIPSIK (pasamos el historial acumulado)
    # Excluimos el último mensaje del usuario del historial porque lo agregamos dentro de la función
    respuesta = genera_respuesta(prompt, st.session_state.messages[:-1])

    # Guardar y mostrar respuesta del bot
    st.session_state.messages.append({"role": "assistant", "content": respuesta})
    with st.chat_message("assistant"):
        st.markdown(respuesta)

# Botón para limpiar el chat
if st.button("🧹 Limpiar chat"):
    st.session_state.messages = [
        {"role": "assistant", "content": "¡Hola humano! Soy Zorp, tu tutor de programación 👽. ¿En qué puedo ayudarte hoy?"}
    ]
    st.rerun()