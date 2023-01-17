import streamlit as st
import os.path

st.subheader("학생사진촬영")

col1, col2 = st.columns(2)

hakbun = col1.text_input("학번")
name = col2.text_input("이름")

pic = st.camera_input("사진찍기")

if pic:
    st.image(pic)

file_path = os.path.dirname(__file__)
pic_path = os.path.join(file_path, 'pics')

if not os.path.exists(pic_path):
    os.mkdir(pic_path)

if pic is not None:
    pic.name = hakbun+name
    fname, ext = os.path.splitext(pic.name)
    with open(os.path.join(pic_path, fname+ext), 'wb') as f:
        f.write(pic.getbuffer())
