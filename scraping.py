from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sys
import pandas as pd  # Import pandas untuk menyimpan ke Excel

# Pastikan Python menggunakan UTF-8 agar tidak error saat mencetak karakter Unicode
sys.stdout.reconfigure(encoding="utf-8")

# Setup WebDriver dengan mode headless
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Mode tanpa tampilan browser
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(options=options)

# Masukkan URL video YouTube
url = "https://youtu.be/IErzvc76fVM?si=Zr976yVXZ-tqD3YG"  # Ganti dengan link YouTube
driver.get(url)

time.sleep(5)  # Tunggu agar halaman termuat

# Scroll ke bawah untuk memuat lebih banyak komentar
scroll_count = 50  # Meningkatkan jumlah scroll agar lebih banyak komentar dimuat
for _ in range(scroll_count):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(1.5)  # Tunggu sejenak agar komentar termuat

# Ambil semua komentar yang sudah termuat
comments = driver.find_elements(By.CSS_SELECTOR, "#content-text")

# Simpan komentar ke dalam list
clean_comments = [comment.text.strip() for comment in comments if comment.text.strip()]

# Ambil hanya 200 komentar pertama
selected_comments = clean_comments[:200]  # Batasi hingga 200 komentar

# Buat DataFrame dengan pandas
df = pd.DataFrame({"Komentar": selected_comments})

# Simpan ke file Excel
file_path = "komentar_youtube.xlsx"
df.to_excel(file_path, index=False, engine="openpyxl")

print(f"\n[✅] Berhasil menyimpan {len(selected_comments)} komentar ke {file_path}")

# Tutup browser setelah selesai
driver.quit()
