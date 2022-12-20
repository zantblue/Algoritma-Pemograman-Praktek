import mysql.connector
import matplotlib.pyplot as plt

db = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "",
    database = "db_mahasiswa",
)
myCursor = db.cursor()
# sql = "SELECT * FROM tb_data"
# myCursor.execute(sql)
# result = myCursor.fetchall()
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
