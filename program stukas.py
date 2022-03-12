# input : suku bunga, lama investasi, arus kas pemasukan dan pengeluaran suatu periode, pemasukan tambahan, dan pengeluaran tambahan.
#output : PV Benefit, PV cost, nilai BCR, kelayakan proyek, total pemasukan dan pengeluaran.

#Login
j = 0
userpass = {'admin' : '123'}
while j < 3:
    username = str(input('Masukkan Username : '))
    password = str(input('Masukkan Password : '))
    if username in userpass and password == userpass[username] and j >= 0:
        print('Login Berhasil!')
        print('=' * 50)
        break
    else:
        j += 1
        print('Login Gagal!')
if j == 3:
    print('Keluar dari Program....')
    quit()

# Halaman awal
menghitungkembali = 'yes'
while menghitungkembali == 'yes':
    print('Selamat datang di kalkulator BCR!')
    print("=" * 50)

    #Input data
    print('Silahkan masukkan data sesuai instruksi!')
    lama_investasi = int(input("Masukkan lama investasi (tahun) : "))
    suku_bunga = int(input("Masukkan suku bunga arus kas pemasukan (x%) : "))
    print('=' * 50)

    #Arus Kas Pemasukan
    x = 0
    y = 0
    kas_pemasukan = []
    kas_pengeluaran = []

    print('---ARUS KAS PEMASUKAN---')
    for x in range(0, lama_investasi + 1):
        print('Periode ke', x)
        aruskas_pemasukan = int(input("Masukkan arus kas pemasukan : "))
        print('Arus kas pemasukan pada periode ke', x, '=', aruskas_pemasukan)
        kas_pemasukan.append(aruskas_pemasukan)
        print('=' * 50)
        x += 1

    print('---ARUS KAS PENGELUARAN---')
    for y in range(0, lama_investasi + 1):
        print('Periode ke', y)
        aruskas_pengeluaran = int(input("Masukkan arus kas pengeluaran : "))
        print('Arus kas pengeluaran pada periode ke', y, '=', aruskas_pengeluaran)
        kas_pengeluaran.append(aruskas_pengeluaran)
        print('=' * 50)
        y += 1

    print('Arus Kas Pemasukan :\n', kas_pemasukan)
    print('Arus Kas Pengeluaran :\n', kas_pengeluaran)

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

    print('PV Benefit Per Periode :\n', pvbenefit_perperiode)
    print('PV Cost Per Periode :\n', pvcost_perperiode)
    print('Total Nilai PV Benefit :\n', sigmapvbenefit)
    print('Total Nilai PV Cost :\n', sigmapvcost)

    #Menghitung bcr
    bcr = float(sigmapvbenefit/sigmapvcost)
    print('Nilai BCR :\n', "{:.2f}".format(bcr))
    if bcr >= 1:
        print('Nilai BCR =', "{:.2f}".format(bcr), "dan Proyek Investasi dapat diterima atau layak.")
    else:
        print('Nilai BCR =', "{:.2f}".format(bcr), "dan Proyek Investasi tidak dapat diterima atau tidak layak.")
    print('=' * 50)

    #Perhitungan pemasukan tambahan
    jenispemasukan_tambahan = []
    pemasukan_tambahan = []
    inputpemasukan_tambahan = str(input("Apakah ada pemasukan tambahan? (yes/no) : ")).lower()
    while inputpemasukan_tambahan == "yes" : 
        variabel_pemasukantambahan = str(input("Masukkan variabel pemasukan tambahan : "))
        nilai_pemasukantambahan = int(input("Masukkan nilai pemasukan tambahan : "))
        lama_pemasukantambahan = int(input("Berapa kali/lama (tahun) pemasukan tambahan didapatkan : "))
        totalnilai_pemasukantambahan = nilai_pemasukantambahan * lama_pemasukantambahan
        jenispemasukan_tambahan.append(variabel_pemasukantambahan)
        pemasukan_tambahan.append(totalnilai_pemasukantambahan)
        inputpemasukan_tambahan = str(input("Apakah ada pemasukan tambahan lain? (yes/no) : ")).lower()
    print(jenispemasukan_tambahan)
    print(pemasukan_tambahan)

    #Perhitungan pengeluaran tambahan
    jenispengeluaran_tambahan = []
    pengeluaran_tambahan = []
    inputpengeluaran_tambahan = str(input("Apakah ada pengeluaran tambahan? (yes/no) : ")).lower()
    while inputpengeluaran_tambahan == "yes" :
        variabel_pengeluarantambahan = str(input("Masukkan variabel pengeluaran tambahan : "))
        nilai_pengeluarantambahan = int(input("Masukkan nilai pengeluaran tambahan : "))
        lama_pengeluarantambahan = int(input("Berapa kali/lama (tahun) pengeluaran tambahan dikeluarkan : "))
        totalnilai_pengeluarantambahan = nilai_pengeluarantambahan * lama_pengeluarantambahan
        jenispengeluaran_tambahan.append(variabel_pengeluarantambahan)
        pengeluaran_tambahan.append(totalnilai_pengeluarantambahan)
        inputpengeluaran_tambahan = str(input("Apakah ada pengeluaran tambahan lain? (yes/no) : ")).lower()
    print(jenispengeluaran_tambahan)
    print(pengeluaran_tambahan)
    print('=' * 50)

    #Total pemasukan dan pengeluaran
    total_pemasukan = sigmapvbenefit + sum(pemasukan_tambahan)
    total_pengeluaran = sigmapvcost + sum(pengeluaran_tambahan)
    print(total_pemasukan)
    print(total_pengeluaran)

    #Tampilkan Arus Kas Pemasukan, Arus Kas Pengeluaran, Present Value Cost, dan Present Value Benefit per Periode dalam bentuk tabel

    #Tampilkan Jenis dan Nilai Pemasukan dan Pengeluaran tambahan dalam bentuk tabel.

    #Tampilkan Total Pemasukan dan Total Pengeluaran dalam grafik batang.

    #Menghitung Kembali
    menghitungkembali = str(input('Apakah ingin menghitung nilai BCR lain? (yes/no) : ').lower())
    print('=' * 50)
print('Terima Kasih telah menggunakan Kalkulator BCR')