# input : suku bunga, lama investasi, arus kas pemasukan dan pengeluaran suatu periode, pemasukan tambahan, dan pengeluaran tambahan.
#output : PV Benefit, PV cost, nilai BCR, kelayakan proyek, total pemasukan dan pengeluaran.

# login
# print(50*"=")
# userpass = {"Admin ICL":"123"}
# userid = input("masukan username anda: ")
# password = input("masukan password anda: ")


# #halaman awal
# print(50*"=")
# print("selamat datang","pada ICL Hotel")

#input data
suku_bunga = int(input("masukan suku bunga : "))
lama_investasi = int(input("masukan lama investasi : "))
aruskas_pengeluaran = int(input("masukan arus kas pemasukan : "))

#perhitungan pemasukan tambahan
pemasukan_tambahan = input("apakah ada pemasukan tambahan? (yes/no)")
while pemasukan_tambahan == "yes" : 
    variabel_pemasukantambahan = int(input("masukan variabel pemasukan tambahan : "))
    nilai_pemasukantambahan = int(input("masukan nilai pemasukan tambahan : "))
    pemasukan_tambahan = input("apakah ada pemasukan tambahan lain? (yes/no)")

#perhitungan pengeluaran tambahan
pengeluaran_tambahan = input("apakah ada pengeluaran tambahan? (yes/no)")
while pengeluaran_tambahan == "yes" :
    nilai_pengeluarantambahan = int(input("masukan nilai pengeluaran tambahan : "))
    pengeluaran_tambahan = input("apakah ada pengeluaran tambahan lain? (yes/no)")

#menghitung present value cost

