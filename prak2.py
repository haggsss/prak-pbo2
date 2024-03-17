nama = input("nama: ")
nim = input("NIM: ")

print("Program Menghitung Keliling dan Luas Segitiga")

print("\nPilih operasi yang ingin Anda lakukan:")
print("1. Hitung Keliling")
print("2. Hitung Luas")
pilihan = input("Masukkan pilihan (1/2): ")

a = float(input("Masukkan sisi 1: "))
b = float(input("Masukkan sisi 2: "))
c = float(input("Masukkan sisi 3: "))

if a + b > c and a + c > b and b + c > a:
    if pilihan == '1':  # Menghitung keliling
        keliling = a + b + c
        print("Keliling segitiga adalah:", keliling)
        print("Terimakasih telah menggunakan program ini!")
    elif pilihan == '2':  # Menghitung luas
        s = (a + b + c) / 2
        luas = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print("Luas segitiga adalah:", luas)
        print("Terimakasih telah menggunakan program ini!")
    else:
        print("\nPilihan tidak valid.")
else:
    print("\nHalo,", nama, "(NIM:", nim + ")")
    print("Sisi-sisi yang dimasukkan tidak membentuk segitiga.")