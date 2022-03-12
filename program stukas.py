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
print('Selamat datang di kalkulator BCR!')
print("=" * 50)

##Input data
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

print('Arus Kas Pemasukan : ', kas_pemasukan)
print('Arus Kas Pengeluaran : ', kas_pengeluaran)

#Menghitung present value benefit
p = 0
q = 0
sigmapvcost = 0
sigmapvbenefit = 0
pvbenefit_perperiode = []
pvcost_perperiode = []


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

print('PV Benefit Per Periode : ', pvbenefit_perperiode)
print('PV Cost Per Periode : ', pvcost_perperiode)
print('Total Nilai PV Benefit : ', sigmapvbenefit)
print('Total Nilai PV Cost : ', sigmapvcost)

#Menghitung bcr
bcr = float(sigmapvbenefit/sigmapvcost)
print("{:.2f}".format(bcr))

#Perhitungan pemasukan tambahan
pemasukan_tambahan = {}
inputpemasukan_tambahan = str(input("Apakah ada pemasukan tambahan? (yes/no) : ")).lower()
while inputpemasukan_tambahan == "yes" : 
    variabel_pemasukantambahan = str(input("Masukkan variabel pemasukan tambahan : "))
    nilai_pemasukantambahan = int(input("Masukkan nilai pemasukan tambahan : "))
    pemasukan_tambahan[variabel_pemasukantambahan] = nilai_pemasukantambahan
    inputpemasukan_tambahan = str(input("Apakah ada pemasukan tambahan lain? (yes/no) : ")).lower()
print(pemasukan_tambahan)

#Perhitungan pengeluaran tambahan
pengeluaran_tambahan = {} 
inputpengeluaran_tambahan = str(input("Apakah ada pengeluaran tambahan? (yes/no) : ")).lower()
while inputpengeluaran_tambahan == "yes" :
    variabel_pengeluarantambahan = str(input("Masukkan variabel pengeluaran tambahan : "))
    nilai_pengeluarantambahan = int(input("Masukkan nilai pengeluaran tambahan : "))
    pengeluaran_tambahan[variabel_pengeluarantambahan] = nilai_pengeluarantambahan
    inputpengeluaran_tambahan = str(input("Apakah ada pengeluaran tambahan lain? (yes/no) : ")).lower()
print(pengeluaran_tambahan)