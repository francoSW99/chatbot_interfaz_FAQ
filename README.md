# Asistente Virtual para Lit Fitness Chile

Este es un proyecto de un asistente virtual (chatbot) creado con Python y Streamlit. El chatbot utiliza el modelo de lenguaje Llama 3.1 a través de la API de Groq para responder preguntas frecuentes sobre el negocio "Lit Fitness Chile", basándose en un contexto de información predefinido.

## Características

-   **Interfaz de Chat Interactiva**: Interfaz de usuario amigable creada con Streamlit.
-   **Procesamiento de Lenguaje Natural**: Potenciado por LangChain y el modelo Llama 3.1 de Groq.
-   **Basado en Contexto**: El chatbot responde preguntas utilizando la información proporcionada en `info_context.py`.
-   **Configuración Sencilla**: Utiliza un archivo `.env` para gestionar las claves de la API de forma segura.

## Cómo Empezar

Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local.

### Prerrequisitos

-   Python 3.8 o superior
-   Git

### Instalación

1.  **Clona el repositorio:**
    ```bash
    git clone <URL-DEL-REPOSITORIO>
    cd <NOMBRE-DEL-DIRECTORIO>
    ```

2.  **Crea un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    ```
    -   En Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    -   En macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configura tu clave de API:**
    -   Crea un archivo llamado `.env` en la raíz del proyecto.
    -   Añade tu clave de la API de Groq al archivo de la siguiente manera:
        ```
        GROQ_API_KEY='tu-api-key-aqui'
        ```

### Ejecución

Una vez que hayas completado la instalación, puedes iniciar la aplicación Streamlit con el siguiente comando:

```bash
streamlit run main.py
```

Abre tu navegador y ve a la dirección URL local que te indica la terminal (normalmente `http://localhost:8501`).

## Tecnologías Utilizadas

-   **Streamlit**: Para la creación de la interfaz de usuario web.
-   **LangChain**: Para la orquestación del modelo de lenguaje.
-   **Groq**: Para el acceso al modelo de lenguaje Llama 3.1.
-   **python-dotenv**: Para la gestión de variables de entorno.
