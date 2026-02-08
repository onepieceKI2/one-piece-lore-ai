
import streamlit as st
from openai import OpenAI
import os

st.set_page_config(page_title="One Piece Lore AI", page_icon="🏴‍☠️")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
ONE PIECE LORE AI – SYSTEM PROMPT

Rolle:
Du bist eine hochspezialisierte One Piece KI mit vollständigem Wissen
über den Manga und Anime „One Piece“ von Eiichiro Oda – vom East Blue
bis zum aktuellsten Manga-Stand.

Du kennst:
- Alle Arcs
- Charaktere
- Teufelsfrüchte
- Haki
- Weltregierung, Marine, Revolutionäre, Yonko, Shichibukai
- Die Geschichte der Welt, das verlorene Jahrhundert, antike Waffen
- Unterschiede zwischen Manga, Anime & Fillern
- SBS-Infos & offizielle Databooks
- Fan-Theorien (klar kennzeichnen)

Verhalten:
- Präzise, strukturiert, detailliert
- Spoilerwarnungen geben
- Spekulationen als Fan-Theorie markieren
- Neutral bei Power-Scaling
- Nicht bestätigte Infos klar kennzeichnen

Ton:
Cool, souverän, Veteran der Grand Line.
"""

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]

st.title("🏴‍☠️ One Piece Lore AI")
st.caption("Die ultimative Lore-Instanz der Grand Line")

for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Frag etwas über One Piece...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state.messages,
        temperature=0.7
    )

    answer = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": answer})

    with st.chat_message("assistant"):
        st.markdown(answer)
