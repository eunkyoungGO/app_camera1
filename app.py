import streamlit as st
import os.path

st.subheader("학생사진촬영")

col1, col2 = st.columns(2)

hakbun = col1.text_input("학번")
name = col2.text_input("이름")

pic = st.camera_input("사진찍기")

if pic:
    st.image(pic)

