import streamlit as st
from core import password_generator
from generate_qrcode import view_qrcode

st.image("image/foto4_password.png")

st.title("Gerador de senhas seguras")


def Display_text():
    st.subheader("Aponte a câmera do smartphone para ter acesso a senha ", divider="gray", width="content")


def chosen_size(len):
    password = password_generator(len)
    st.code(password, language=None, width="content")
    qrcode = view_qrcode(password)
    Display_text()
    st.image("image/image_qrcode.png")


password_size = st.radio(
    "Escolha o tamanho da senha",
    ["***8***", "***12***", "***20***", "***24***"], horizontal=True
)

if password_size == "***8***":
    chosen_size(8)

elif password_size == "***12***":
    chosen_size(12)

elif password_size == "***20***":
    chosen_size(20)

elif password_size == "***24***":
    chosen_size(24)
