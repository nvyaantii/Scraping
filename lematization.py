import pandas as pd
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

# Load hasil stemming
df = pd.read_excel("hasil_stemming.xlsx")

# Lemmatization
df['Lemmatized'] = df['Stemmed'].apply(
    lambda tokens: [lemmatizer.lemmatize(t) for t in eval(tokens)]
)

df.to_excel("hasil_lemmatization.xlsx", index=False)

print("✅ Lematisasi selesai. Disimpan di 'hasil_lemmatization.xlsx'")