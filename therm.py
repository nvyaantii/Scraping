import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# Load hasil lemmatization
df = pd.read_excel("hasil_lemmatization.xlsx")

# Gabungkan list lemmatized menjadi string
df['Text'] = df['Lemmatized'].apply(lambda x: ' '.join(eval(x)))

# Gunakan CountVectorizer untuk term frequency
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['Text'])

# Buat DataFrame dari hasil vectorizer
terms_df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

# Gabungkan dengan data awal jika perlu
final_df = pd.concat([df, terms_df], axis=1)

# Simpan ke file Excel
final_df.to_excel("hasil_term.xlsx", index=False)

print("✅ Term extraction selesai. Disimpan di 'hasil_term.xlsx'")
