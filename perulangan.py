# 1. Perulangan FOR menggunakan range()
print("=== Perulangan FOR (1 sampai 5) ===")
for i in range(1, 6):
    print(f"Iterasi ke-{i}")

# 2. Perulangan WHILE (hitung mundur)
print("\n=== Perulangan WHILE (Hitung Mundur) ===")
hitung = 5
while hitung > 0:
    print(f"Waktu tersisa: {hitung} detik")
    hitung -= 1  # Mengurangi nilai hitung sebesar 1 setiap putaran

print("Selesai!")
