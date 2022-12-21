import mysql.connector
import matplotlib.pyplot as plt

db = mysql.connector.connect(
    user = "root",
    password = "",
    host = "127.0.0.1",
    database = "db_kuliah"
)
myCursor = db.cursor()

def tampilData():
    sql = "SELECT * FROM tb_mahasiswa"
    myCursor.execute(sql)
    hasil = myCursor.fetchall()
    for j in hasil:
        print("NIM : ",j[1])
        print("Nama : ",j[2])
        print("Nilai Alpro : ",j[3])
        print("Nilai Agama : ",j[4])
        print("Nilai TBO : ",j[5])
        print("="*20)

def inputAdmin():
    sql = "INSERT INTO tb_mahasiswa(nim,nama,nilai_alpro,nilai_agama,nilai_tbo) VALUES(%s,%s,%s,%s,%s)"
    data = []
    nim = input("Masukan NIM : ")
    nama = input("Masukan Nama : ")
    nilai_alpro = input("Masukan Nilai Alpro : ")
    nilai_agama = input("Masukan Nilai Agama : ")
    nilai_tbo = input("Masukan Nilai TBO : ")
    data.append(nim)
    data.append(nama)
    data.append(nilai_alpro)
    data.append(nilai_agama)
    data.append(nilai_tbo)
    myCursor.execute(sql,data)
    db.commit()
    
def cariData():
    sql = "SELECT * FROM tb_mahasiswa"
    myCursor.execute(sql)
    hasil = myCursor.fetchall()
    print("1. Cari Data Berdasarkan NIM")
    print("2. Cari Data Berdasarkan Nama")
    pilih = input("Pilih Menu : ")
    if pilih == '1':
        nim = input("Masukan NIM yang ingin dicari : ")
        for j in hasil:
            if j[1] == nim:
                print("NIM : ",j[1])
                print("Nama : ",j[2])
                print("Nilai Alpro : ",j[3])
                print("Nilai Agama : ",j[4])
                print("Nilai TBO : ",j[5])
                print("="*20)
                break
        else:
            print("Data Tidak ditemukan")
    elif pilih == '2':
        nama = input("Masukan Nama yang ingin dicari : ")
        for j in hasil:
            if j[2] == nama:
                print("NIM : ",j[1])
                print("Nama : ",j[2])
                print("Nilai Alpro : ",j[3])
                print("Nilai Agama : ",j[4])
                print("Nilai TBO : ",j[5])
                print("="*20)
                break
        else:
            print("Data Tidak ditemukan")
    else:
        print("Menu Tidak Tersedia Dikembalikan ke Menu Utama")
def admin():
    password = input("Luwak White Coffee Passwordnya : ")
    if password != "admin123":
        print("Password Salah !!!")
        return True
    else:
        while True:
            print("1. Input Data")
            print("2. Tampilkan Semua Data")
            print("3. Cari Data")
            print("4. Kembali ke Menu Utama")
            pilih = input("Pilih Menu : ")
            if pilih == '1':
                inputAdmin()
            elif pilih == '2':
                tampilData()
            elif pilih == '3':
                cariData()
            elif pilih == '4':
                print("Kembali Ke Menu Utama")
                return True
            else :
                print("Menu Tidak Tersedia")
def tampilDataMhs():
    sql = "SELECT * FROM tb_mahasiswa"
    myCursor.execute(sql)
    hasil = myCursor.fetchall()
    nim = input("Masukan NIM yang ingin dicari : ")
    for j in hasil:
        if j[1] == nim:
            print("NIM : ",j[1])
            print("Nama : ",j[2])
            print("Nilai Alpro : ",j[3])
            print("Nilai Agama : ",j[4])
            print("Nilai TBO : ",j[5])
            print("="*20)
            break
    else:
        print("Data Tidak ditemukan")
def tampilGraph():
    sql = "SELECT * FROM tb_mahasiswa"
    myCursor.execute(sql)
    hasil = myCursor.fetchall()
    nim = input("Masukan NIM : ")
    for j in hasil:
        if j[1] == nim:
            sql = "SELECT * FROM tb_matkul"
            myCursor.execute(sql)
            data = myCursor.fetchone()
            nama = []
            nama.append(data[1])
            nama.append(data[2])
            nama.append(data[3])
            nilai = j[3:]
            plt.bar(nama,nilai)
            plt.show()
    else:
        print("Data Tidak ditemukan")
def mahasiswa():
    while True:
        print("1. Lihat Data Berdasarkan NIM")
        print("2. Tampilkan Graphic Nilai")
        print("3. Kembali ke Menu Utama")
        pilih = input("Pilih Menu : ")
        if pilih == '1':
            tampilDataMhs()
        elif pilih == '2':
            tampilGraph()
        elif pilih == '3':
            print("Kembali Ke Menu Utama")
            return True
        else :
            print("Menu Tidak Tersedia")

while True:
    print("1. Menu Admin")
    print("2. Menu Mahasiswa")
    print("3. Exit")
    pilih = input("Pilih Menu : ")
    if pilih == '1':
        admin()
    elif pilih == '2':
        mahasiswa()
    elif pilih == '3':
        exit()
    else:
        print("Menu Tidak Tersedia Dikembalikan ke Menu Utama")
