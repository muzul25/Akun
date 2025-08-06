import streamlit as st
import pandas as pd

st.title("Pencarian Username & Password")

try:
    # Coba baca file dengan delimiter koma
    df = pd.read_csv("database.csv")
except pd.errors.ParserError:
    try:
        # Coba lagi dengan delimiter titik koma
        df = pd.read_csv("database.csv", delimiter=';')
    except Exception as e:
        st.error(f"Gagal membaca file database.csv: {e}")
        st.stop()


# Form pencarian username
username_input = st.text_input("Masukkan Username:")

# Tombol cari
if st.button("Cari"):
    result = df[df['Username'].str.lower() == username_input.lower()]

    if not result.empty:
        selected_data = result.iloc[0][['Nama', 'Username', 'Password']]
        st.success("Data ditemukan!")
        st.write("### Hasil Pencarian:")
        st.write(f"**Nama:** {selected_data['Nama']}")
        st.write(f"**Username:** {selected_data['Username']}")
        st.write(f"**Password:** {selected_data['Password']}")
    else:
        st.warning("Username tidak ditemukan.")
        

@st.cache_data
def load_data():
    return pd.read_csv("database.csv")

df = load_data()



