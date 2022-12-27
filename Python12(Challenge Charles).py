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

def LihatData():
    sql = "SELECT * FROM tb_karyawan"
    myCursor.execute(sql)
    hasil = myCursor.fetchall()
    for i in hasil:
        print("Nama :",i[1])
        print("Kode Karyawan :",i[2])
        print("Jenis Karyawan :",i[3])

def InputData():
    sql = "INSERT INTO tb_karyawan(nama,kode_karyawan,jenis)VALUES(%s,%s,%s)"
    data = []
    nama = input("Masukan Nama : ")
    kode = input("Masukan Kode Karyawan : ")
    jenis = input("Masukan Jenis Karyawan : ")
    data.append(nama)
    data.append(kode)
    data.append(jenis)
    myCursor.execute(sql,data)
    db.commit()

def CariData():
    sql = "SELECT * FROM tb_karyawan"
    myCursor.execute(sql)
    hasil = myCursor.fetchall()
    print("1. Cari Data Berdasarkan Nama")
    print("2. Cari Data Berdasarkan Kode Karyawan")
    pilih = input("Pilih Menu : ")
    if pilih == "1":
        nama = input("Masukan NIM yang ingin dicari : ")
        for i in hasil:
            if i[1] == nama:
                print("Nama :",i[1])
                print("Kode Karyawan :",i[2])
                print("Jenis Karyawan :",i[3])
                print("="*20)
                break
        else:
            print("Data Tidak ditemukan")
    elif pilih == '2':
        kode = input("Masukan kode yang ingin dicari : ")
        for i in hasil:
            if i[2] == kode:
                print("Nama :",i[1])
                print("Kode Karyawan :",i[2])
                print("Jenis Karyawan :",i[3])
                print("="*20)
                break
        else:
            print("Data Tidak ditemukan")
    else:
        print("Menu Tidak Tersedia Dikembalikan ke Menu Utama")

def Admin():
    password = input("Password anda : ")
    if password != "123":
        print("PASSWORD SALAH !!!")
        return True
    else:
        while True: 
            print("1. Input Data Karyawan")
            print("2. Lihat Data Karyawan")
            print("3. Cari Data Karyawan")
            print("4. Kembali Ke Menu Sebelumnya")
            print("="*20)
            pilih = input("Pilih Menu : ")
            if pilih == "1":
                InputData()
            elif pilih == "2":
                LihatData()
            elif pilih == "3":
                CariData()
            elif pilih == "4":
                print("Kembali Ke Menu Sebelumnya")
                return True
            else:
                print("Menu Tidak Tersedia")

#def WaktuLembur():

def Karyawan():
    sql = "SELECT * FROM tb_karyawan"
    myCursor.execute(sql)
    Karyawan = myCursor.fetchall()
    Nama = input("Nama : ")
    Kode = input("Kode Karyawan : ")
    for i in Karyawan:
        if i[1] == Nama and i[2] == Kode:
            print("<===== LOGIN BERHASIL! ======>")
            print("1. Input Waktu Lembur Perjam")
            print("2. Lihat Gaji Karyawan")
            print("3. Kembali Ke Menu Utama")
            pilih = input("Pilih Menu : ")
            if pilih == "1":
                WaktuLembur()
            elif pilih == "2":
                LihatGaji()
            elif pilih == "3":
                print("Kembali Ke Menu Sebelumnya")
            else:
                print("Menu Tidak Tersedia")



while True:
    print("="*20)
    print("1. Admin")
    print("2. Karyawan")
    print("3. Exit")
    pilih = input("Pilih Menu : ")
    if pilih == "1":
        Admin()
    elif pilih == "2":
        Karyawan()
    elif pilih == "3":
        exit()
    else:
        print("Menu Tidak tersedia! Kembali ke Menu Utama")
