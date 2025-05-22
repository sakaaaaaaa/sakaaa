import streamlit as st

st.title("🙈sakaageraldine")
st.write(
    "akuu saka aku bangga jadi anak mamah"
)
st.image("view/867ac950-7979-4560-8422-63d873a5662c.jpeg",width=200)


st.header("aplikasi mengecek nilai genap/ganjil")
angka = st.number_input("tulis sebuah angka:", value=0, step=1)

if (angka % 2) == 0:
 st.writer(f"{angka} adalah bilangan genap")
else:
 st.writer(f"{angka} adalah bilangan ganjil")
