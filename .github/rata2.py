# seleksi nilai para siswa

'''
    jumlah siswa = 30
    nilai rata rata = 78
'''

jumlah_siswa = 30
rata_rata = 78

angka = [
    20, 20, 20, 80, 90,70,30,20,10,100,
    20, 30, 20, 80, 90,70,30,20,10,100,
    20, 20, 20, 80, 90,70,30,20,10,100
]
'''
for i in range(jumlah_siswa):
    print(i)'''
hitung = 0
for i in range(jumlah_siswa):
    if angka[i] > rata_rata:
        hitung += 1
print("jumlah siswa diatas rata rata = ", hitung)