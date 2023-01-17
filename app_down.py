import streamlit as st
import os.path

file_path = os.path.dirname(__file__)
pic_path = os.path.join(file_path, 'pics')

if not os.path.exists(pic_path):
    os.mkdir(pic_path)

if pic is not None:
    pic.name = hakbun+name
    fname, ext = os.path.splitext(pic.name)
    with open(os.path.join(pic_path, fname+ext), 'wb') as f:
        f.write(pic.getbuffer())
