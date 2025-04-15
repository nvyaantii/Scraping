import pandas as pd
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# Setup stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# Load hasil stopwords
df = pd.read_excel("hasil_stopwords_removal.xlsx")

# Stemming
df['Stemmed'] = df['No_Stopwords'].apply(
    lambda tokens: [stemmer.stem(t) for t in eval(tokens)]
)

df.to_excel("hasil_stemming.xlsx", index=False)

print("✅ Stemming selesai. Disimpan di 'hasil_stemming.xlsx'")