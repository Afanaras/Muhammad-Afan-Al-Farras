data_angka = []

angka = ''

while True:
    inputan  = input("Masukkan Angka: (Ketik exit untuk keluar) ")

    if inputan == "exit":
        break

    try:
        angka = int(inputan)
        data_angka.append(angka)
    except ValueError:
        print("Maaf yang anda masukkan bukan angka")
    

from pathlib import Path

contents = ""
for angka in data_angka:
    contents += str(angka) + "\n"

path = Path('C:/Users/HP/Downloads/data_angka.txt')
path.write_text(contents)
    

# print("Daftar Nama: ")
# for n in daftar_nama:
#     print(n)
