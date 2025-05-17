## Library virtual environment
```
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source env/bin/activate    #Linux/Mac
venv\Scripts\activate       #Windows

# Install the required packages
pip install -r requirements.txt
```

## Menjalani streamlit
```
# run streamlit
streamlit run main.py
```

## Notes
1. Markdown guide: https://www.markdownguide.org/
2. perbedaan st.table dengan st.dataframe
   - st.table: menampilkan data dalam bentuk tabel statis, tidak bisa di-scroll
   - st.dataframe: menampilkan data dalam bentuk tabel interaktif, bisa di-scroll dan di-sort
3. st.start_time: waktu mulai detik ke- streamlit dijalankan
4. default st.write -> False sampai tekan button
5. streamlit emoji: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
6. st.session_state.disabled: menyimpan state dari streamlit jika True maka button tidak bisa di-klik
7. st.slider = (100, 1000, 100) = (min, max, default)
8. st.empty = untuk mengganti konten yang ada di dalamnya. Jadi tidak ditulis baris per baris namun langsung diganti sampi loop habis dan hilang.

Multiple pages:
1. Folder pages ke luar dari venv/
```
02_streamlit/
├── main.py
├── pages/
│   ├── javascript_tutorial.py
│   ├── java_tutorial.py
│   └── python_tutorial.py
├── venv/
```
2. Jalankan streamlit tanpa harus mengaktifkan venv


.env
```
Fungsi load_dotenv() digunakan untuk memuat variabel lingkungan (environment variables) dari file .env ke dalam aplikasi Python kamu. Ini sangat berguna saat kamu ingin menyimpan informasi rahasia seperti:
1. API keys
2. Token akses
3. Password database
4. Konfigurasi sensitif lainnya
```