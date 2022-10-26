##Challenge 1
tinggi = 10
alas = 5
Luas = alas * tinggi 

tinggi = int (input("tinggi : "))
alas = int (input("alas : "))
Luas = tinggi * alas /2
print("Luas",Luas)

##Challenge 2
sisiAtas = input("masukan sisiAtas :")
sisiBawah = input("masukan sisiBawah :")
tinggi = input("masukan tinggi :")

Luas = int(int(tinggi)*int(sisiAtas + sisiBawah)/2)
print(int(Luas))

##Challenge 3
nilai = input("masukkan nilai ")
nilai = int(nilai)
if nilai >100:
    print("nilai yang dimasukkan 0-100")
elif nilai >80:
    print("nilai A")
elif nilai >60:
    print("nilai B")
elif nilai >40:
    print("nilai C")
elif nilai >20:
    print("nilai D")
elif nilai >0:
    print("nilai E")
else:
    print("Nilai yang dimasukkan 0-100")
    
##Challenge 4
pembeli = input("Masukan jumlah belanja : ")
pembeli = int(pembeli)
if pembeli >= 100000:
    diskon = 10/100
else :
    diskon = 5/100
hitung = pembeli * diskon
total = pembeli - hitung
print("diskon :",hitung)
print("harga setelah diskon :", total)

#Challenge 5
for i in range(2,41):
    if i == 10:
        print("ini adalah nilai",i)
        continue
    elif i == 20:
        print("ini adalah nilai",i)
        continue
    elif i == 30:
        print("ini adalah nilai",i)
        break
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

pilih = int(input(" Bagun datar \n[1] Luas segitiga\n[2] Luas lingkaran\n[3] Luas Persegi\n[>]Pilih bangun datar :"))
if pilih == 1:
    luasSegitiga()
elif pilih == 2:
    luasLingkaran()
elif pilih == 3:
    luasPersegi()

#Challenge 6
    #mencari data berdasarkan nim, nim berdasarkan imputan dari user
dataNIM = int(input("Masukan NIM yang anda cari :"))

data = [
        [500411291, "Faiz"],
        [500411292, "Nazhir"],
        [500411293, "Amrulloh"],
        [500411294, "Reza"],
        [500411295, "Saputra"]
]
        
for i in data:
    if i[0] == dataNIM:
        print(i)
        break
