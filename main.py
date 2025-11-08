import streamlit as st
from core import password_generator
from generate_qrcode import view_qrcode

st.image("image/foto4_password.png")

st.title("Gerador de senhas seguras")

def Display_text():
    st.subheader("Aponte a câmera do smartphone para ter acesso a senha ", divider="gray", width="content")

password_size = st.radio(
    "Escolha o tamanho da senha",
    ["***8***", "***12***", "***20***", "***24***"], horizontal=True
)

if password_size == "***8***":
    password = password_generator(8)
    st.code(password, language=None, width="content")
    qrcode = view_qrcode(password)
    Display_text()
    st.image("image/image_qrcode.png")


elif password_size == "***12***":
    password = password_generator(12)
    st.code(password, language=None, width="content")
    qrcode = view_qrcode(password)
    Display_text()
    st.image("image/image_qrcode.png")

elif password_size == "***20***":
    password = password_generator(20)
    st.code(password, language=None, width="content")
    qrcode = view_qrcode(password)
    Display_text()
    st.image("image/image_qrcode.png")

elif password_size == "***24***":
    password = password_generator(24)
    st.code(password, language=None, width="content")
    qrcode = view_qrcode(password)
    Display_text()
    st.image("image/image_qrcode.png")
