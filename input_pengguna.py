# Mengambil input teks (otomatis bertipe str)
nama = input("Masukkan nama panggilan kamu: ")

# Mengambil input angka dan mengubahnya menjadi integer dengan int()
tahun_lahir = int(input("Masukkan tahun lahir kamu: "))

# Menghitung perkiraan umur di tahun 2026
umur = 2026 - tahun_lahir

print(f"Halo {nama}! Di tahun 2026 ini umur kamu sekitar {umur} tahun.")
print("Tipe data variabel umur:", type(umur))
