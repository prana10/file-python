# coba seleksi nilai para siswa
'''
diketahui   :
    jumlah siswa nya ada 30
    nilai rata rata 78

perintah :
    cari siswa yang diatas rata rata
'''
jumlah_siswa = 30
rata_rata = 78

info_nilai = [
    20, 20, 20, 80, 90,70,30,20,10,100,
    20, 30, 20, 80, 90,70,30,20,10,100,
    20, 20, 20, 80, 90,70,30,20,10,100
]

hitung = 0
for i in list(info_nilai):
    print(i)
for i in range(jumlah_siswa):
    if info_nilai[i]> rata_rata:
        hitung += 1
print("jumlah siswa yang diatas rata rata: ", hitung)