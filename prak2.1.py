# Mendapatkan 2 digit terakhir dari NIM
nim = input("Masukkan NIM Anda: ")
last_two_digits = nim[-2:]

print("Deret angka dari 1 sampai 50 (kecuali 2 digit terakhir dari NIM):")

# Melakukan iterasi dari 1 sampai 50
for i in range(1, 51):
    # Memeriksa apakah angka saat ini adalah 2 digit terakhir dari NIM
    if str(i) == last_two_digits:
        continue  # Lewati iterasi jika angka adalah 2 digit terakhir dari NIM
    print(i, end=" ")  # Cetak angka jika bukan 2 digit terakhir dari NIM
