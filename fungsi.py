# 1. Fungsi sederhana tanpa nilai kembalian (return)
def sapa_pengguna(nama, waktu="pagi"):
    print(f"Halo {nama}, selamat {waktu}! Semangat belajar Python-nya.")

# 2. Fungsi dengan nilai kembalian (return)
def hitung_luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    return luas

# Memanggil fungsi
sapa_pengguna("Neisya")
sapa_pengguna("Neisya", "siang")

hasil_luas = hitung_luas_persegi_panjang(12, 5)
print(f"\nLuas persegi panjang (12 x 5) adalah: {hasil_luas} cm²")
