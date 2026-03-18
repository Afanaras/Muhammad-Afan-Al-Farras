print("selamat datang di penjumlahan angka sederhana")
print("\nketik exit untk keluar")

while True:
    angka1 = input("\nMasukkan Angka pertama: ")
    if angka1.lower() == "exit":
        break

    angka2 = input("Masukkan angka kedua: ")
    if angka2.lower() == "exit":
        break

    try:
        jawab = int(angka1) / int(angka2)
    except ValueError:
        print("Maaf angka yang anda masukkan tidak valid")
    else:
        print(jawab)
