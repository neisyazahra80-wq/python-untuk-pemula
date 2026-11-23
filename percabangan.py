nilai = int(input("Masukkan nilai ujian kamu (0-100): "))

if nilai >= 90:
    predikat = "A (Sangat Baik)"
elif nilai >= 80:
    predikat = "B (Baik)"
elif nilai >= 70:
    predikat = "C (Cukup)"
elif nilai >= 60:
    predikat = "D (Kurang)"
else:
    predikat = "E (Tidak Lulus)"

print(f"Nilai kamu {nilai}, mendapatkan predikat: {predikat}")
