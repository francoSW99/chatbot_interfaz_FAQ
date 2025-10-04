import streamlit as st
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from info_context import info
import os
from dotenv import load_dotenv

load_dotenv()

# --- Configuración de la página ---
st.set_page_config(page_title="Lit Fitness Chile - Asistente Virtual", layout="centered")

# --- Configuración del Modelo ---
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

try:
    model = ChatGroq(groq_api_key=GROQ_API_KEY, model="llama-3.1-8b-instant")
except Exception as e:
    st.error(f"Error al conectar con Groq: {e}")
    model = None

# --- Lógica Principal del Chat ---
st.title("Lit Fitness Chile - Asistente Virtual")

# Template de la plantilla
template = '''
Answer the question below in Spanish, based on the provided business information and conversation history.

Here is the business information for FAQ interaction:
{info_context}

Here is the context of the conversation:
{context}

Here is the question:
{question}

Answer:
'''
prompt = PromptTemplate.from_template(template)

# Inicializar el historial del chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensajes del historial
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Lógica de la cadena y la entrada de chat
if model:
    chain = prompt | model

    if user_question := st.chat_input("Escríbele a nuestro asistente..."):
        # Mostrar y guardar mensaje del usuario
        with st.chat_message("user"):
            st.markdown(user_question)
        st.session_state.messages.append({"role": "user", "content": user_question})

        # Construir el contexto
        context = "\n".join([f'{msg["role"]}: {msg["content"]}' for msg in st.session_state.messages])

        # Invocar la cadena
        with st.spinner("Pensando..."):
            result_chunk = chain.invoke({
                "context": context,
                "question": user_question,
                "info_context": info
            })
            
            # Langchain v0.2.0 devuelve un AIMessage, extraemos el contenido
            result = result_chunk.content if hasattr(result_chunk, 'content') else str(result_chunk)

        # Mostrar y guardar respuesta del bot
        with st.chat_message("assistant"):
            st.markdown(result)
        st.session_state.messages.append({"role": "assistant", "content": result})
else:
    st.error("No se pudo inicializar el asistente. Verifica la API Key o la conexión.")
    st.chat_input("Escríbele a nuestro asistente...", disabled=True)
