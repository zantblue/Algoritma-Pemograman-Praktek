import os
dataMaster = []

def inputData():
    nama = input("Masukkan Nama Anda : ")
    npm = input("Masukkan NIM Anda : ")
    nilaiAgama = input("Masukan Nilai Agama anda : ")
    nilaiAlpro = input("Masukan Nilai Alpro anda : ")
    nilaiMatematika = input("Masukan Nilai Matematika anda : ")
    dataSlave = []
    try:
        int(nilaiAgama)
    except:
        print("Nilai yang ")
    if type(int(nilaiAgama)) == int :
        print ("tes")
    dataSlave.append(nama)
    dataSlave.append(npm)
    dataSlave.append(nilaiAgama)
    dataSlave.append(nilaiAlpro)
    dataSlave.append(nilaiMatematika)
    dataMaster.append(dataSlave)
    print(dataMaster)

def SemuaData():
    if dataMaster == []:
        print("Data Masih Belum tersedia")
    else:
        print("="*30)
        for i in dataMaster:
            print("Nama : ",i[0])
            print("NPM : ",i[1])
            print("Nilai Alpro : ",i[2])
            print("Nilai Matematika : ",i[3])
            print("Nilai Agama : ",i[4])
            print("="*30)
def tampilNPM():
    if dataMaster == []:
        print("Data Masih Belum tersedia")
    else:
        print("="*30)
        NIM = input("Masukkan NPM yang Datanya ingin dicari : ")
        for i in dataMaster:
            if i[1] == NIM:
                print("Nama : ",i[0])
                print("NPM : ",i[1])
                print("Nilai Alpro : ",i[2])
                print("Nilai Matematika : ",i[3])
                print("Nilai Agama : ",i[4])
                print("="*30)
                break
            else:
                print("NPM yang anda cari tidak ada")

def tampilNilai():
    if dataMaster == []:
        print("Data Masih Belum tersedia")
    else:
        print("="*30)
        print("1. Nilai Alpro")
        print("1. Nilai Matematika")
        print("1. Nilai Agama")
        pilih = input("Pilih Nilai yang Ingin dicari Datanya : ")
        if pilih == "1":
            nama = "Nilai Alpro"
        elif pilih == "2":
            nama = "Nilai Matematika"
        elif pilih == "3":
            nama = "Nilai Agama"
        else:
            return print("Nama yang dimasukan tidak sesuai")

        pilih = int(pilih)
        for i in dataMaster:
            if i[1] == nama:
                print("Nama : ",i[0])
                print("NPM : ",i[1])
                print("Nilai Alpro : ",i[pilih+1])
                print("="*30)
                break
            else:
                print("NPM yang anda cari tidak ada")

def tampilNama():
    if dataMaster == []:
        print("Data Masih Belum tersedia")
    else:
        print("="*30)
        nama = input("Masukkan Nama yang Datanya ingin dicari : ")
        for i in dataMaster:
            if i[0] == nama:
                print("Nama : ",i[0])
                print("NPM : ",i[1])
                print("Nilai Alpro : ",i[2])
                print("Nilai Matematika : ",i[3])
                print("Nilai Agama : ",i[4])
                print("="*30)
                break
            else:
                print("nama yang anda cari tidak ada")

def cariNPM():
    if dataMaster == []:
        print("Data Masih Belum tersedia")
    else:
        print("="*30)
        NIM = input("Masukkan NPM yang Ingin Dicari Datanya: ")
        for i in dataMaster:
            if i[1] == NIM:
                print("Nama : ",i[0])
                print("NPM : ",i[1])
                print("Nilai Alpro : ",i[2])
                print("Nilai Matematika : ",i[3])
                print("Nilai Agama : ",i[4])
                print("="*30)
                break
            else:
                print("NPM yang anda cari tidak ada")

def cariNama():
    if dataMaster == []:
        print("Data Masih Belum tersedia")
    else:
        print("="*30)
        NIM = input("Masukkan NPM yang Ingin Dicari Datanya: ")
        for i in dataMaster:
            if i[1] == NIM:
                print("="*30)
                print("Nama : ",i[0])
                print("NPM : ",i[1])
                print("Nilai Alpro : ",i[2])
                print("Nilai Matematika : ",i[3])
                print("Nilai Agama : ",i[4])
                print("="*30)
                break
            else:
                print("NPM yang anda cari tidak ada")

def hapusData():
    if dataMaster == []:
        print("Data Masih Belum tersedia")
    else:
        print("="*30)
        NIM = input("Masukkan NPM yang Ingin Dicari Datanya: ")
        for i in dataMaster:
            if i[1] == NIM:
                dataMaster.remove(i)
                print("Data Telah Dihapus")
                print("="*30)
                break
            else:
                print("NPM yang anda cari tidak ada")

def editData():
    if dataMaster == []:
        print("Data Masih Belum tersedia")
    else:
        print("="*30)
        NIM = input("Masukkan NPM yang Datanya ingin dicari : ")
        for i in dataMaster:
            if i[1] == NIM:
                print("="*30)
                print("Nama : ",i[0])
                print("NPM : ",i[1])
                print("Nilai Alpro : ",i[2])
                print("Nilai Matematika : ",i[3])
                print("Nilai Agama : ",i[4])
                print("="*30)
                i[2] = input("Masukan Nilai Alpro Anda : ")
                i[3] = input("Masukan Nilai Matematika Anda : ")
                i[4] = input("Masukan Nilai Agama Anda : ")
                
                print("Data Berhasil Diubah")
                break
            else:
                print("NPM yang anda cari tidak ada")

while True:
    print("="*30)
    print("1. Input data")
    print("2. Tampilkan Semua Data")
    print("3. Tampilkan Data berdasarkan NPM")
    print("4. Tampilkan Data berdasarkan Nama")
    print("5. Tampilkan Data berdasarkan Nilai")
    print("6. Cari Data berdasarkan NPM")
    print("7. Cari Data berdasarkan Nama")
    print("8. Hapus Data berdasarkan NPM")
    print("9. Edit Data berdasarkan Nama")
    print("10. Exit")
    print("="*30)
    pilihan = input("Piih Menu yang tersedia : ")
    if pilihan == "1":
        inputData()
    elif pilihan == "2":
        SemuaData()
    elif pilihan == "3":
        tampilNPM()
    elif pilihan == "4":
        tampilNama()
    elif pilihan == "5":
        tampilNilai()
    elif pilihan == "6":
        cariNPM()
    elif pilihan == "7":
        cariNama()
    elif pilihan == "8":
        hapusData()
    elif pilihan == "9":
        editData()
    elif pilihan == "10":
        exit()
    else:
        print("Maaf data yang anda cari tidak ada")
