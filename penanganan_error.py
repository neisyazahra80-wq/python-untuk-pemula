print("=== Kalkulator Pembagian Aman ===")

try:
    angka1 = int(input("Masukkan angka pembilang: "))
    angka2 = int(input("Masukkan angka penyebut : "))
    hasil = angka1 / angka2
except ValueError:
    print("Error: Input harus berupa angka bulat, bukan huruf!")
except ZeroDivisionError:
    print("Error: Angka tidak bisa dibagi dengan nol (0)!")
else:
    print(f"Hasil pembagian {angka1} / {angka2} = {hasil}")
finally:
    print("Program selesai dijalankan.")
