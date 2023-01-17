import streamlit as st
import os.path

st.subheader("학생사진촬영")

col1, col2 = st.columns(2)

hakbun = col1.text_input("학번")
name = col2.text_input("이름")

pic = st.camera_input("사진찍기")

if pic:
    st.image(pic)

    img_path=os.path.join(os.path.dirname(__file__),'images')
    if not os.path.exists(img_path):
        os.mkdir(img_path)

    uploaded_file=st.file_uploader("이미지선택",type=['jpg','png'])

