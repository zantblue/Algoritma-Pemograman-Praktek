#Fungsi atau sub program atau method atau sub routine

#Default penulisan fungsi 
# def namaFungsi():
#     badan fungsi

#Contoh 1
def printNama():
    print("Nama saya adalah Mizard")

printNama()

#Contoh 2
def luasPersegi():
    sisi = 10 
    luas = sisi * sisi 
    print(f"Luas persegi adalah {luas}")

#luasPersegi()

#Contoh 3
def LuasPersegiInput():
   sisi = int(input("Masukkan panjang sisi"))
   luas = sisi * sisi
   print(f"Luas persegi adalah {luas}")

#Fungsi menggunakan prameter / argument

#Contoh 1
def luasPersegi(sisi):
  luas = sisi * sisi
  print(f"Luas persegi adalah {luas}")
luasPersegi(20)

#Contoh 2
def luasSegitiga(alas, tinggi):
   luas = alas * tinggi / 2
   print(f"Luas persegi adalah {luas}")
luasSegitiga(10,20)

#Fungsi menggunakan return 
def Persegi(sisi):
    luas = sisi * sisi
    return luas

tampung = Persegi(10)
print(tampung)

def kalkulator(angka_satu, angka_dua):
    tambah = angka_satu + angka_dua
    kurang = angka_satu - angka_dua
    kali = angka_satu * angka_dua
    bagi = angka_satu / angka_dua
    return tambah, kurang, kali, bagi

# a,b,c,d = kalkulator(10,5)
print(a)
print(b)
print(c)
print(d)

#Default parameter atau argument
def tambah(angka1=10, angka2=5, angka3=15):
    proses = angka1 + angka2 + angka3
    print("hasilnya adalah", proses)

tambah(angka2=20)

#Challenge 6
def luasSegitiga():
    alas = int(input("Masukkan panjang alas = "))
    tinggi = int(input("Masukkan panjang tinggi = "))
    luas = alas * tinggi /2
    print(f"Luas Segitiga adalah {luas}")

def luasLingkaran():
    jari = int(input("Masukkan panjang jari-jari = "))
    luas = 3.14 * jari * jari
    print(f"Luas Lingkaran adalah {luas}")

def luasPersegi():
    sisi = int(input("Masukkan panjang sisi = "))
    luas = sisi * sisi 
    print("Luas persegi adalah", luas)

pilih = int(input(" Bagun datar \n[1] Luas segitiga\n[2] Luas lingkaran\n[3] Luas Persegi\n[>] Pilih bangun datar :"))
if pilih == 1:
    luasSegitiga()
elif pilih == 2:
    luasLingkaran()
elif pilih == 3:
    luasPersegi()
