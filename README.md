# 👽💻 Chatbot Tutor de Programación — Zorp

> Proyecto realizado por **TofuDev (José Alberto Ávila Pérez)**

Un chatbot interactivo con inteligencia artificial que actúa como tutor de programación. Está impulsado por el modelo **DeepSeek** y construido con **Streamlit**, accesible desde el navegador gracias a un túnel de **Cloudflare**.

---

## 🛸 ¿Quién es Zorp?

Zorp es un alien amigable del planeta **Xylos-9** que responde tus preguntas sobre programación de forma clara, breve y con ejemplos de código. No olvida los emojis espaciales. 👽🚀🪐

---

## ⚙️ Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| [Streamlit](https://streamlit.io/) | Interfaz web del chatbot |
| [DeepSeek API](https://platform.deepseek.com/) | Modelo de lenguaje (LLM) |
| [OpenAI SDK](https://github.com/openai/openai-python) | Cliente compatible con DeepSeek |
| [pycloudflared](https://github.com/piccolo-orm/pycloudflared) | Túnel público para exponer la app |

---

## 🚀 Instalación y ejecución

Este proyecto está diseñado para correr en **Google Colab** o cualquier entorno con Python.

### 1. Instalar dependencias

```bash
pip install pycloudflared streamlit openai
```

### 2. Configurar tu API Key de DeepSeek

Abre el archivo `SimpleChat.py` y reemplaza el valor de `api_key` con tu clave:

```python
client = OpenAI(
    api_key="TU_API_KEY_AQUÍ",
    base_url="https://api.deepseek.com"
)
```

> ⚠️ **Nunca compartas tu API key públicamente ni la subas a repositorios.**

### 3. Levantar el servidor

```python
from pycloudflared import try_cloudflare
tunnel = try_cloudflare(port=8501)
print(f"Accede aquí: {tunnel.tunnel}")
```

```bash
streamlit run SimpleChat.py --server.port 8501
```

---

## 📁 Estructura del proyecto

```
📦 proyecto-zorp/
 ┣ 📄 SimpleChat.py        # App principal de Streamlit
 ┗ 📄 README.md            # Este archivo
```

---

## 🧠 ¿Cómo funciona?

1. El usuario escribe una pregunta en el chat.
2. La app envía el historial completo de la conversación + la nueva pregunta a la API de DeepSeek.
3. DeepSeek responde como **Zorp**, un tutor alienígena de programación.
4. La respuesta se muestra en pantalla y se guarda en el historial de sesión de Streamlit.

El historial se mantiene activo durante la sesión gracias a `st.session_state`. El botón 🧹 **Limpiar chat** reinicia la conversación desde cero.

---

## 💡 Personalización

Puedes modificar el comportamiento de Zorp editando el `system prompt` dentro de la función `genera_respuesta`:

```python
{
    "role": "system",
    "content": (
        "Eres Zorp, un alien amigable y divertido del planeta Xylos-9. "
        "Tu objetivo es responder preguntas sobre temas de programación. "
        "Responde de forma clara, breve y con ejemplos de código cuando sea útil."
    )
}
```

---

## 📌 Notas

- El modelo utilizado es `deepseek-chat`. Puedes cambiarlo a otros modelos disponibles en DeepSeek según tu plan.
- El streaming está desactivado (`stream=False`). Puedes activarlo para una experiencia más fluida.
- Si la API falla, Zorp mostrará un mensaje de error amigable en lugar de crashear la app.

---

## 📜 Licencia

Proyecto educativo de uso libre. Puedes modificarlo y compartirlo con crédito al autor original.

**TofuDev — José Alberto Ávila Pérez** 🛸
