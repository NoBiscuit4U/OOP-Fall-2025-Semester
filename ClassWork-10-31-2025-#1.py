import streamlit as st
from PIL import Image

img=Image.open(r"C:\Users\braggd\Downloads\labwork-3.drawio.png")
col1,col2=st.columns(spec=[0.3,0.3],vertical_alignment="top")

with col1:
    st.title("Resume")
    st.header("**Daniel Bragg**")

    st.divider()
    st.markdown("**About Me**")
    st.text("I am a Machine Learning enthusiast with a passion for automation and ethics.")

    st.divider()
    st.markdown("**Education**")
    st.text("")

    st.divider()
    st.markdown("**Projects**")
    st.text("")

    st.divider()
    st.markdown("**Hobbies**")
    st.text("")

    st.divider()
    st.markdown("**Contact Me**")
    st.text("")
    st.text_input("Name")
    st.text_input("Email")
    st.text_input("Message")
    st.button("Submit")

with col2:
    st.image(img, width=200)
