import pandas as pd
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

stop_words = set(stopwords.words('indonesian')) | set(stopwords.words('english'))

# Load hasil tokenisasi
df = pd.read_excel("hasil_tokenisasi.xlsx")
# Hapus stopwords
df['No_Stopwords'] = df['Tokens'].apply(
    lambda tokens: [t for t in eval(tokens) if t.lower() not in stop_words]
)

# Simpan hasil
df.to_excel("hasil_stopwords_removal.xlsx", index=False)

print("✅ Stopwords removal selesai. Disimpan di 'hasil_stopwords_removal.xlsx'")