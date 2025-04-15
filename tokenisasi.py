import nltk

# Download tokenizer yang diperlukan
nltk.download('punkt')
nltk.download('punkt_tab')  # Jika error, abaikan

# Baru lanjutkan ke kode tokenisasi...

import pandas as pd
import nltk
from nltk.tokenize import word_tokenize

# Pastikan nltk punkt sudah terunduh
nltk.download('punkt')

# Load file komentar mentah
df = pd.read_excel("Scraping.xlsx")

# Periksa apakah kolom "Komentar" ada dalam file
if "Komentar" not in df.columns:
    raise ValueError("Kolom 'Komentar' tidak ditemukan di dalam file Excel.")

# Tokenisasi
df['Tokens'] = df['Komentar'].dropna().astype(str).apply(lambda x: word_tokenize(x))

# Simpan hasil tokenisasi
df.to_excel("hasil_tokenisasi.xlsx", index=False)

print("✅ Tokenisasi selesai. Disimpan di 'hasil_tokenisasi.xlsx'")
