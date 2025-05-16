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