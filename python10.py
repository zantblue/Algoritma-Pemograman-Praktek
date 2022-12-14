import mysql.connector

db = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "",
    database = "db_alpro"
)
myCursor = db.cursor()

def mahasiswa():
    data = []
    NPM = input("masukan NPM : ")
    Nama_mahasiswa = input("masukan Nama Anda : ")
    data.append(NPM)
    data.append(Nama_mahasiswa)
    sql = "INSERT INTO tb_mahasiswa (NPM, Nama_mahasiswa) VALUES (%s,%s)"
    myCursor.execute(sql,data)
    db.commit()

def nilai():
    data = []
    bahasa_indonesia = input("masukan nilai Bahasa Indonesia: ")
    android = input("masukan nilai Android: ")
    TBO = input("masukan nilai TBO: ")
    data.append(bahasa_indonesia)
    data.append(android)
    data.append(TBO)
    sql = "INSERT INTO tb_nilai (bahasa_indonesia, android, TBO) VALUES (%s,%s,%s)"
    myCursor.execute(sql,data)
    db.commit()

while True:
    print("Menu")
    print("Menu")
    print("1. Input data mahasiswa")
    print("2. Input Nilai")
    print("3. Exit")
    pilihan = input("Pilih Menu Yang Tersedia : ")
    if pilihan == '1':
        mahasiswa()
    elif pilihan == '2':
        nilai()
    elif pilihan == '3':
        exit()
