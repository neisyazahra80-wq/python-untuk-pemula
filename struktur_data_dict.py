# Membuat dictionary data mahasiswa/siswa
profil = {
    "nama": "Neisya",
    "umur": 17,
    "jurusan": "Rekayasa Perangkat Lunak",
    "aktif": True
}

print("Data awal:", profil)
print("Nama:", profil["nama"])
print("Jurusan:", profil["jurusan"])

# Menambah dan mengubah data
profil["kota"] = "Bandung"
profil["umur"] = 18

# Menampilkan seluruh key dan value dengan perulangan
print("\n=== Detail Profil Terbaru ===")
for kunci, nilai in profil.items():
    print(f"{kunci.capitalize()} : {nilai}")
