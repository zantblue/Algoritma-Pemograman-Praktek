import mysql.connector
import matplotlib.pyplot as plt

db = mysql.connector.connect(
    user = "root",
    password = "",
    host = "127.0.0.1",
    database = "db_perusahaan"
)
myCursor = db.cursor()
upahLembur = 10000
def getJenis(id = ''):
    if id != '':
        sql = "SELECT * FROM tb_jenis"
        myCursor.execute(sql)
        jenis = myCursor.fetchall()
        for i in jenis:
            if i[0] == id:
                return i
    else:
        sql = "SELECT * FROM tb_jenis"
        myCursor.execute(sql)
        return myCursor.fetchall()

def tambahKaryawan():
    data = []
    sql = "INSERT INTO tb_karyawan (nama,kode_karyawan,jenis) VALUES (%s,%s,%s)"
    nama = input("Masukan Nama : ")
    kode = input("Masukan Kode Karyawan : ")
    jenisKaryawan = getJenis()
    for i in jenisKaryawan:
        print(i[0],'. ',i[1])
    jenis = input("Pilih Jenis Karyawan : ")
    data.append(nama)
    data.append(kode)
    data.append(jenis)
    myCursor.execute(sql,data)
    db.commit()

def tampilKaryawan():
    sql = "SELECT * FROM tb_karyawan"
    myCursor.execute(sql)
    karyawan =  myCursor.fetchall()
    for i in karyawan:
        jenis = getJenis(i[3])
        print('='*16)
        print("Nama Karyawan  : ",i[1])
        print("Kode Karyawan  : ",i[2])
        print("Jenis Karyawan : ",jenis[1])
        print('='*16)

def cariKaryawan():
    sql = "SELECT * FROM tb_karyawan"
    myCursor.execute(sql)
    karyawan =  myCursor.fetchall()
    print("-"*30)
    kode = input("Masukan Kode Karyawan : ")
    for i in karyawan:
        if i[2] == kode:
            jenis = getJenis(i[3])
            print('='*16)
            print("Nama Karyawan  : ",i[2])
            print("Kode Karyawan  : ",i[1])
            print("Jenis Karyawan : ",jenis[1])
            print('='*16)
            break
    else:
        print("Data Tidak Ditemukan")

def tampilGraph():
    jenis = getJenis()
    sql_count_grup = "SELECT COUNT(nama),jenis FROM tb_karyawan GROUP BY jenis"
    myCursor.execute(sql_count_grup)
    test = myCursor.fetchall()
    data = []
    for i in test:
        data.append(i[0])
    nama_jenis = []
    for i in jenis:
        nama_jenis.append(i[1])
    plt.bar(nama_jenis,data)
    plt.show()


def admin():
    pw = input("Masukan Password : ")
    if pw != "123":
        print("Paswword Salah !!!")
    else:
        print("<===================>")
        print("LOGIN BERHASIL!")
        print("1. Input Data Karyawan")
        print("2. Lihat Semua Data Karyawan")
        print("3. Cari Karyawan")
        print("4. Lihat Grafik")
        print("-"*30)
        pilih = input("Pilih Menu : ")
        if pilih == '1':
            tambahKaryawan()
        elif pilih == '2':
            tampilKaryawan()
        elif pilih == '3':
            cariKaryawan()
        elif pilih == '4':
            tampilGraph()
        else:
            print("Menu Tidak Tersedia")

def karyawan():
    sql = "SELECT * FROM tb_karyawan"
    myCursor.execute(sql)
    karyawan =  myCursor.fetchall()
    nama = input("Masukan Nama : ")
    kode = input("Masukan Kode Karyawan : ")
    for i in karyawan:
        if i[1] == nama and i[2] == kode:
            print("Login Berhasil!")
            print("1. Lembur")
            print("2. Tampilkan Gaji")
            print("-"*30)
            pilih = input("Pilih Menu : ")
            jenis = getJenis(i[3])
            lembur = 0
            if pilih == '1':
                lembur = input("Masukan Waktu Lembur : ")
                print("Lembur Anda : ",upahLembur*int(lembur))
            elif pilih == '2':
                gaji = jenis[2]
                print("^"*30,gaji)
                print("Gaji Anda             : ",gaji)
                print("Total Pendapatan Anda : ",int(gaji) + upahLembur * int(lembur))
            else:
                print("Menu Tidak Tersedia")

while True:
    print("<===== Menu Perusahaan =====>")
    print("1. Admin")
    print("2. Karyawan")
    print("3. Exit")
    print("-"*30)
    pilih = input("Pilih Menu : ")
    if pilih == '1':
        admin()
    elif pilih == '2':
        karyawan()
    elif pilih == '3':
        exit()
