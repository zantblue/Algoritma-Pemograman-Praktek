import mysql.connector

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
        for j in jenis:
            if j[0] == id:
                return j
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
    for j in jenisKaryawan:
        print(j[0],'. ',j[1])
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
    for j in karyawan:
        jenis = getJenis(j[3])
        print(j[2])
        print(j[1])
        print(jenis[1])

def cariKaryawan():
    sql = "SELECT * FROM tb_karyawan"
    myCursor.execute(sql)
    karyawan =  myCursor.fetchall()
    kode = input("Masukan Kode Karyawan : ")
    for j in karyawan:
        if j[2] == kode:
            jenis = getJenis(j[3])
            print(j[2])
            print(j[1])
            print(jenis[1])
            break
    else:
        print("Data Tidak Ditemukan")
        
def admin():
    pw = input("Masukan Password : ")
    if pw != "":
        print("Paswword Salah !!!")
    else:
        print("1. Input Nama, Kode Karyawan dan Jenis Karyawan")
        print("2. Lihat Semua Data Karyawan")
        print("3. Cari Karyawan")
        pilih = input("Pilih Menu : ")
        if pilih == '1':
            tambahKaryawan()
        elif pilih == '2':
            tampilKaryawan()
        elif pilih == '3':
            cariKaryawan()
        else:
            print("Menu Tidak Tersedia")

def karyawan():
    sql = "SELECT * FROM tb_karyawan"
    myCursor.execute(sql)
    karyawan =  myCursor.fetchall()
    nama = input("Masukan Nama : ")
    kode = input("Masukan Kode Karyawan : ")
    for j in karyawan:
        if j[1] == nama and j[2] == kode:
            print("Login Berhasil")
            print("1. Lembur")
            print("2. Tampilkan Gaji")
            pilih = input("Pilih Menu : ")
            jenis = getJenis(j[3])
            lembur = 0
            if pilih == '1':
                lembur = input("Masukan Waktu Lembur : ")
                print("Lembur Anda : ",upahLembur*int(lembur))
            elif pilih == '2':
                gaji = jenis[2]
                print("Gaji Anda : ",gaji)
                print("Total Pendapatan Anda : ",int(gaji) + upahLembur * int(lembur))
            else:
                print("Menu Tidak Tersedia")


while True:
    print("1. Admin")
    print("2. Karyawan")
    pilih = input("Pilih Menu : ")
    if pilih == '1':
        admin()
    elif pilih == '2':
        karyawan()
