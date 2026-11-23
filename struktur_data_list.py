# Membuat list awal
bahasa = ["Python", "JavaScript", "C++", "Rust"]

print("Daftar awal:", bahasa)
print("Elemen pertama (index 0):", bahasa[0])
print("Elemen terakhir (index -1):", bahasa[-1])

# Menambah elemen baru dengan append()
bahasa.append("Go")
print("\nSetelah ditambah 'Go':", bahasa)

# Menghapus elemen dengan remove()
bahasa.remove("C++")
print("Setelah 'C++' dihapus:", bahasa)

# Menampilkan semua isi list dengan perulangan
print(f"\nTotal bahasa pemrograman: {len(bahasa)}")
for item in bahasa:
    print("-", item)
