"""
judul   : list(python)
(materi lanjutan pada python)

list terdapat beberapa metode(method)  :
1. menambahkan list
2. menghapus list
3. membalik
4. mengurut
5. memotong
6. operasi list
7. list multidimensi

"""

# materi 1. menambahkan list
"""
    pada materi ini, ada 3 method untuk menambahkan list
1. prepend (menambahkan dari depan)  (tapi karena ada kendala, method prepend tidak bisa digunakan)
2. append (menambahkan dari belakang)
3. insert (menambahkan sesuai index)

"""
print("materi pertama")
print("\n")
#append
buah = ["mangga", "durian", "apel", "semangka"]
buah.append("manggis")
print (buah)
print("\n")

#insert
nomor = [1,2,3,4,5,6]
nomor.insert(6, 6)
print (nomor)
print("\n")

print("materi ke dua")


#materi 2 menghapus item di list
"""
ada 3 cara menghapus item di list
1. pake del
2. pake .remove()
3. pake .pop() (ini digunakan untuk menghapus bagian akhir saja)
"""
print("\n")
#kita siapkan sebuah list bernama hewan_laut
hewan_laut = ["ikan hiu", "ikan pari", "ikan piranha", "ikan paus"]

#cara 1 menggunakan del
del hewan_laut[1]
print (hewan_laut)
print("\n")

#cara 2 menggunakan .remove()
hewan_laut.remove("ikan hiu")
print(hewan_laut)

#cara 3 menggunakan .pop
hewan_laut.pop()
print (hewan_laut)
print("\n")

print("materi ke 3")
#materi ke 3 membalik list
#hanya ada 1 cara yaitu menggunakan .reverse()

print("\n")
#siapkan list nya
x = [5, 4, 3, 2, 1]
x.reverse()
print(x)

print('materi ke 4')
#materi 4 mengurut list
# materi ini hanya ada 1 cara yaitu menggunakan .sort()

print('\n')
#siapkan list nya
z = [4, 6, 9, 1, 2, 3, 5, 8]
z.sort()
print(z)
print("\n")

#materi ke 5
print('materi ke 5')
#di materi ini kita akan memotong item pada list

print("\n")
a = [1,2,3,4,5,6,7,8]
print (a [2: 7])
print("\n")

print('materi ke 6')
# materi ke 6
"""
 pada materi kali ini ada beberapa cara untuk menggunakan operasi list
yaitu menggunakan (penggabungan) dan (perkalian)
"""
print("\n")
#contoh penggabungan
print("contoh penggabungan pada operasi list")
list_lagu = [
    "no women",
    "dear god"
]

lagu_pavorit = [
    "op naruto"
]

semua_lagu = list_lagu + lagu_pavorit
print(semua_lagu)
print("\n")

#contoh perkalian/perulangan pada list
list_anime = [
    "naruto"
]
ulangi = 5

sekarang = list_anime * ulangi
print(sekarang)
