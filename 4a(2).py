daftar_nama = []

nama = ''

while True:
    nama  = input("Masukkan Nama Anda: (Ketik exit untuk keluar) ")

    if nama.lower() == "exit":
        break

    daftar_nama.append(nama)

from pathlib import Path

contents = ""
for nama in daftar_nama:
    contents += nama + "\n"

path = Path('C:/Users/HP/Downloads/guest_book.txt')
path.write_text(contents)
    

# print("Daftar Nama: ")
# for n in daftar_nama:
#     print(n)
