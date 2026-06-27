import streamlit as st
import time

from tools import get_joke


# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="😂 Joke AI Agent Pro",
    page_icon="😂",
    layout="centered"
)

# -------------------------
# TITLE
# -------------------------
st.title("😂 Joke AI Agent Pro")
st.write("Just type anything — I will automatically tell a joke 😎")

# -------------------------
# CHAT MEMORY
# -------------------------
if "chat" not in st.session_state:
    st.session_state.chat = []


# -------------------------
# DISPLAY CHAT HISTORY
# -------------------------
for role, msg in st.session_state.chat:
    if role == "user":
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg)


# -------------------------
# USER INPUT
# -------------------------
user_input = st.chat_input("Type your message...")

if user_input:

    # Show user message
    st.session_state.chat.append(("user", user_input))
    st.chat_message("user").write(user_input)

    # -------------------------
    # LOADING ANIMATION
    # -------------------------
    with st.spinner("Finding a joke for you... 😂"):
        time.sleep(0.8)
        response = get_joke(user_input)

    # -------------------------
    # TYPING ANIMATION
    # -------------------------
    placeholder = st.empty()
    typed_text = ""

    for char in response:
        typed_text += char
        placeholder.markdown(f"**{typed_text}**")
        time.sleep(0.02)

    # Save response
    st.session_state.chat.append(("assistant", response))