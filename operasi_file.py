nama_file = "catatan_belajar.txt"

# 1. Menulis file baru (mode 'w')
with open(nama_file, "w", encoding="utf-8") as file:
    file.write("=== Log Belajar Python ===\n")
    file.write("1. Dasar sintaks & variabel\n")
    file.write("2. Percabangan & perulangan\n")

# 2. Menambah baris baru ke file (mode 'a')
with open(nama_file, "a", encoding="utf-8") as file:
    file.write("3. Struktur data, fungsi & file handling\n")

# 3. Membaca kembali isi file (mode 'r')
print(f"Membaca isi dari '{nama_file}':\n")
with open(nama_file, "r", encoding="utf-8") as file:
    isi = file.read()
    print(isi)
