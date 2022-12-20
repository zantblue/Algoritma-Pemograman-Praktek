###Challenge 1
tinggi = 10
alas = 5
Luas = alas * tinggi 

tinggi = int (input("tinggi : "))
alas = int (input("alas : "))
Luas = tinggi * alas /2
print("Luas",Luas)

###Challenge 2
sisiAtas = input("masukan sisiAtas :")
sisiBawah = input("masukan sisiBawah :")
tinggi = input("masukan tinggi :")

Luas = int(int(tinggi)*int(sisiAtas + sisiBawah)/2)
print(int(Luas))

###Challenge 3
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
    
###Challenge 4
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

###Challenge 5
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
        
###Challenge 6
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

###Challenge 9
import numpy as np

data1 = (10,'mizard',20,30,40)
data2 = ('5220411093',50,60,70,80,90)
#data3 = np.array([50,60,70,80,90])
a = data1 [0:1]
b = data1 [2:]
c = data2 [1:5]
angka1 = np.array(a+b)
angka2 = np.array(c)
hasil = angka1 + angka2

#Hasil = data2[2], data2[4], data2[5]+data1[0], data2[5]+data1[3] 
#+ data2[1], data2[4], data1[0] + data2[6]
print("Nama :",data1[1])
print("NIM :",data2[0])
print("Result :",hasil)

###Challenge10
import numpy as np

data1 = (1,2,3,4,'mizard',"5220411093",5,6,7,8,9,10)
data2 = (11,'18',12,13,14,15,16,17,18,19,20)
a = data1 [0:4]
b = data1 [6:]
c = data2 [0:1]
d = data2 [2:]
genap =[]
ganjil = []
angka1 = a+b
angka2 = c+d
hasil = angka1 + angka2

for i in hasil:
    if i %2 == 0:
        genap.append(i) 
    else:
        ganjil.append(i)
        
print("Nama :",data1[4])
print("NIM :",data2[5])
print("umur :",data2[1])
print(len(genap))
print(len(ganjil))

###Challenge11
import mysql.connector
import matplotlib.pyplot as plt

db = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "",
    database = "db_mahasiswa",
)
myCursor = db.cursor()
data = []
def mahasiswa():
    Nama = input("masukan Nama Anda : ")
    NIM = input("masukan NPM : ")
    data.append(Nama)
    data.append(NIM)
    sql = "INSERT INTO tb_data (Nama, NIM) VALUES (%s,%s)"
    myCursor.execute(sql, data)
    db.commit()

def tampil():
    sql = "SELECT * FROM tb_data"
    myCursor.execute(sql)
    result = myCursor.fetchall()
    for i in result:
        print(i)

def TampilNamaNim():
    sql = "SELECT * FROM tb_data"
    myCursor.execute(sql)
    result = myCursor.fetchall()
    for i in result:
        print(i[1],',',i[2])

def cari():
    sql = "SELECT * FROM tb_data"
    myCursor.execute(sql)
    cari = input("Masukan NIM : ")
    result = myCursor.fetchall()
    for i in result:
        if i[2]== cari:
            print(i)

def graph():
    sql = "SELECT * FROM tb_nilai"
    myCursor.execute(sql)
    result = myCursor.fetchone()
    nilai = ["agama","bahasa","alpro"]
    print(result)
    plt.bar(nilai,result[1:])
    plt.show()


while True:
    print("========MENU========")
    print("1. Input data")
    print("2. Tampilkan semua data")
    print("3. Tampilkan Nama, NIM")
    print("4. Cari data")
    print("5. tampilkan Grafik")
    print("6. Exit")
    pilihan = input("Pilih Menu Yang Tersedia : ")
    print("========================")
    if pilihan == "1":
        mahasiswa()
    elif pilihan =="2":
        tampil()
    elif pilihan =="3":
        TampilNamaNim()
    elif pilihan =="4":
        cari()
    elif pilihan =="5":
        graph()
    elif pilihan =="6":
        exit()
