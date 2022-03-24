#input : suku bunga, lama investasi, arus kas pemasukan dan pengeluaran suatu periode, pemasukan tambahan, dan pengeluaran tambahan.
#output : PV Benefit, PV cost, nilai BCR, kelayakan proyek, total pemasukan dan pengeluaran.
import time
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#Login
unpw = {'dayyin': '1234','aldi':'4321', 'lea': '0702', 'maura':'6789', 'aji':'5432'}
def login (un,pw):
 if un in unpw and pw == unpw[un] :
    hasil = True
 else :
    hasil = False
 return hasil 
i=3
while  i >= 1:
   un = input('Masukkan Username : ')
   pw = input('Masukkan Password : ')
   hasil=(login(un,pw))
   if hasil == True :
         print('='*10,'SELAMAT ANDA BERHASIL LOGIN','='*10)
         break
   else :
         i-=1
         print('Maaf Login Gagal','\nPercobaan kurang:',i)
if i == 0 :
    print('Keluar dari Program....')
    quit()

# Halaman awal
menghitungkembali = 'yes'
while menghitungkembali == 'yes':
    print('Selamat datang di kalkulator BCR!')
    print("=" * 50)

    #Input data
    print('Silahkan masukkan data sesuai instruksi!')
    while True:
        try:
            lama_investasi = int(input("Masukkan lama investasi (tahun) : "))
            suku_bunga = int(input("Masukkan suku bunga arus kas pemasukan (x%) : "))
            print('=' * 50)
            if lama_investasi and suku_bunga > 0:
                break
            else:
                print('=' * 25)
                print('Nilai Input tidak valid ( < 0)')
                print('=' * 25)
        except ValueError:
            print('=' * 25)
            print("Masukkan nilai berupa Integer")
            print('=' * 25)
            continue

    #Arus Kas Pemasukan
    x = 0
    y = 0
    kas_pemasukan = []
    kas_pengeluaran = []

    print('---ARUS KAS PEMASUKAN---')
    for x in range(0, lama_investasi + 1):
        while True:
            try:
                print('Periode ke', x)
                aruskas_pemasukan = int(input("Masukkan arus kas pemasukan : "))
                if aruskas_pemasukan >= 0:
                    print('Arus kas pemasukan pada periode ke', x, '=', aruskas_pemasukan)
                    kas_pemasukan.append(aruskas_pemasukan)
                    print('=' * 50)
                    x += 1
                    break
                else:
                    print('=' * 25)
                    print('Nilai Input tidak valid ( < 0)')
                    print('=' * 25)
            except ValueError:
                print('=' * 25)
                print("Masukkan nilai berupa Integer")
                print('=' * 25)
                continue

    print('---ARUS KAS PENGELUARAN---')
    for y in range(0, lama_investasi + 1):
        while True:
            try:
                print('Periode ke', y)
                aruskas_pengeluaran = int(input("Masukkan arus kas pengeluaran : "))
                if aruskas_pengeluaran >= 0:
                    print('Arus kas pengeluaran pada periode ke', y, '=', aruskas_pengeluaran)
                    kas_pengeluaran.append(aruskas_pengeluaran)
                    print('=' * 50)
                    y += 1
                    break
                else:
                   print('=' * 25)
                   print('Nilai Input tidak valid ( < 0)')
                   print('=' * 25)
            except ValueError:
                print('=' * 25)
                print("Masukkan nilai berupa Integer")
                print('=' * 25)
                continue

    print('Arus Kas Pemasukan :\n', kas_pemasukan,'\n')
    print('Arus Kas Pengeluaran :\n', kas_pengeluaran,'\n')

    #Menghitung present value benefit
    p = 0
    q = 0
    sigmapvcost = 0
    sigmapvbenefit = 0
    pvbenefit_perperiode = []
    pvcost_perperiode = []

    #Menghitung present value benefit
    for a in kas_pemasukan:
        if p <= lama_investasi:
            pvbenefit = float(a / (((suku_bunga/100 + 1) ** p)))
            sigmapvbenefit += pvbenefit 
            pvbenefit_perperiode.append(pvbenefit)
            p += 1
        else:
            break

    #Menghitung present value cost
    for b in kas_pengeluaran:
        if q <= lama_investasi:
            pvcost = float(b / (((suku_bunga/100 + 1) ** q)))
            sigmapvcost += pvcost
            pvcost_perperiode.append(pvcost)
            q += 1
        else:
            break

    print('PV Benefit Per Periode :\n', pvbenefit_perperiode,'\n')
    print('PV Cost Per Periode :\n', pvcost_perperiode,'\n')
    print('Total Nilai PV Benefit :\n', sigmapvbenefit,'\n')
    print('Total Nilai PV Cost :\n', sigmapvcost,'\n')

    #Menghitung bcr
    bcr = float(sigmapvbenefit/sigmapvcost)
    print('Nilai BCR :\n', "{:.2f}".format(bcr))
    if bcr >= 1:
        print('Nilai BCR =', "{:.2f}".format(bcr), "dan Proyek Investasi dapat diterima atau layak.",'\n')
    else:
        print('Nilai BCR =', "{:.2f}".format(bcr), "dan Proyek Investasi tidak dapat diterima atau tidak layak.",'\n')
    print('=' * 50)

    #Perhitungan pemasukan tambahan
    jenispemasukan_tambahan = []
    pemasukan_tambahan = []
    inputpemasukan_tambahan = str(input("Apakah ada pemasukan tambahan? (yes/no) : ")).lower()
    t1 = 0
    t2 = 0
    while inputpemasukan_tambahan == "yes" :    
            while True:
                try:
                    variabel_pemasukantambahan = str(input("Masukkan variabel pemasukan tambahan : "))
                    nilai_pemasukantambahan = int(input("Masukkan nilai pemasukan tambahan : "))
                    if nilai_pemasukantambahan >= 0:
                        jenispemasukan_tambahan.append(variabel_pemasukantambahan)
                        pemasukan_tambahan.append(nilai_pemasukantambahan)
                        inputpemasukan_tambahan = str(input("Apakah ada pemasukan tambahan lain? (yes/no) : ")).lower()
                        t1 += 1
                        break
                    else:
                        print('=' * 25)
                        print('Nilai Input tidak valid ( < 0)')
                        print('=' * 25)
                except ValueError:
                    print('=' * 25)
                    print("Masukkan integer untuk nilai pemasukan")
                    print('=' * 25)
                    continue
    print(jenispemasukan_tambahan)
    print(pemasukan_tambahan)

    #Perhitungan pengeluaran tambahan
    jenispengeluaran_tambahan = []
    pengeluaran_tambahan = []
    inputpengeluaran_tambahan = str(input("Apakah ada pengeluaran tambahan? (yes/no) : ")).lower()
    
    while inputpengeluaran_tambahan == "yes" :
        while True:
            try:
                variabel_pengeluarantambahan = str(input("Masukkan variabel pengeluaran tambahan : "))
                nilai_pengeluarantambahan = int(input("Masukkan nilai pengeluaran tambahan : "))
                if nilai_pengeluarantambahan >= 0:      
                    jenispengeluaran_tambahan.append(variabel_pengeluarantambahan)
                    pengeluaran_tambahan.append(nilai_pengeluarantambahan)
                    inputpengeluaran_tambahan = str(input("Apakah ada pengeluaran tambahan lain? (yes/no) : ")).lower()
                    t2 += 1
                    break
                else:
                    print('=' * 25)
                    print('Nilai Input tidak valid ( < 0)')
                    print('=' * 25)
            except ValueError:
                print('=' * 25)
                print("Masukkan integer untuk nilai pengeluaran")
                print('=' * 25)
                continue
    print(jenispengeluaran_tambahan)
    print(pengeluaran_tambahan)
    print('=' * 50)

    #Total pemasukan dan pengeluaran
    total_pemasukan = sigmapvbenefit + sum(pemasukan_tambahan)
    total_pengeluaran = sigmapvcost + sum(pengeluaran_tambahan)
    print('Total Pemasukan =', total_pemasukan,'\n')
    print('Total Pengeluaran =', total_pengeluaran,'\n')

    #Tampilkan Arus Kas Pemasukan, Arus Kas Pengeluaran, Present Value Cost, dan Present Value Benefit per Periode dalam bentuk tabel
    tabel = {
        'Arus Kas Pemasukan' : kas_pemasukan,
        'Arus Kas Pengeluaran' : kas_pengeluaran,
        'Present Value Benefit' : pvbenefit_perperiode,
        'Present Value Cost' : pvcost_perperiode
    }
    dataframe = pd.DataFrame(tabel, [0, lama_investasi])
    print(dataframe,'\n')

    #Tampilkan Jenis dan Nilai Pemasukan dan Pengeluaran tambahan dalam bentuk tabel.
    tabel1 = {
        'Variabel Pemasukan Tambahan' : jenispemasukan_tambahan,
        'Nilai Pemasukan Tambahan' : pemasukan_tambahan
    }
    tabel2 = {
        'Variabel Pengeluaran Tambahan' : jenispengeluaran_tambahan,
        'Nilai Pengeluaran Tambahan' : pengeluaran_tambahan
    }
    dataframe1 = pd.DataFrame(tabel1, [1, t1])
    print(dataframe1,'\n')
    dataframe2 = pd.DataFrame(tabel2, [1, t2])
    print(dataframe2,'\n')

    #Tampilkan Total Pemasukan dan Total Pengeluaran dalam grafik batang.
    sbx = ['Total Pemasukan', 'Total Pengeluaran']
    sby = [total_pemasukan, total_pengeluaran]
    plt.title('Grafik Perbandingan Pemasukan dan Pengeluaran')
    plt.bar(sbx, sby)
    plt.show()

    #Menghitung Kembali
    menghitungkembali = str(input('Apakah ingin menghitung nilai BCR lain? (yes/no) : ').lower())
    print('=' * 50)
print('Terima Kasih telah menggunakan Kalkulator BCR')
print('=' * 50)
print('Pengakses : ', un)
time.ctime()
t = time.ctime()
print('Waktu Akses : ', t)
