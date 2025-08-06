import streamlit as st
import pandas as pd

# Load database dari file CSV
df = pd.read_csv("database.csv")

# Judul aplikasi
st.title("Pencarian Username & Password")

# Form pencarian username
username_input = st.text_input("Masukkan Username:")

# Tombol cari
if st.button("Cari"):
    # Filter data berdasarkan username (case-insensitive)
    result = df[df['Username'].str.lower() == username_input.lower()]
    
    if not result.empty:
        # Ambil hanya satu data jika ada beberapa yang cocok
        selected_data = result.iloc[0][['Nama', 'Username', 'Password']]
        st.success("Data ditemukan!")
        st.write("### Hasil Pencarian:")
        st.write(f"**Nama:** {selected_data['Nama']}")
        st.write(f"**Username:** {selected_data['Username']}")
        st.write(f"**Password:** {selected_data['Password']}")
    else:
        st.warning("Username tidak ditemukan.")
