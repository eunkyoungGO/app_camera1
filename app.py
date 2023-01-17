import streamlit as st
import os.path

st.subheader("학생사진촬영")

col1, col2 = st.columns(2)

hakbun = col1.text_input("학번")
name = col2.text_input("이름")

pic = st.camera_input("사진찍기")

img_path = os.path.join(os.path.dirname(__file__), 'images')
uploaded_file = st.file_uploader("이미지선택", type=['jpg', 'png'])

if pic is not None:
    img_name = hakbun+name
    fname, ext = os.path.splitext(pic.name)
    with open(os.path.join(img_path, img_name+ext), 'wb') as f:
        f.write(uploaded_file.getbuffer())
