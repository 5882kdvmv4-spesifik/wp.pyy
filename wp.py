import streamlit as st
import pyqrcode
import png

mail=st.text_input("Gmail adresinizi giriniz:")
telefon="905521507299"
link="https://wa.me/"+telefon+"?text="+mail

qr=pyqrcode.create(link)
qr.png("wp.png", scale=10)

st.image("wp.png")

