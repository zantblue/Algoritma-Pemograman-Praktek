import os
dataMaster = []
# dataMaster = [['Charles Daniel', 5220411080, 100, 100, 100], [
#     'Veranda', 5220411019, 90, 90, 90]]


def convert_int(text):
    try:
        var = int(input(text))
    except:
        var = input(text)
    return var


def inputData():
    os.system('cls')
    print("="*20)
    nama = input("Masukan Nama Anda : ")
    npm = convert_int("Masukan NPM Anda : ")
    nilaiAlpro = convert_int("Masukan Nilai Alpro Anda : ")
    nilaiMatematika = convert_int("Masukan Nilai Matematika Anda : ")
    nilaiAgama = convert_int("Masukan Nilai Agama Anda : ")
    dataSlave = []
    dataSlave.append(nama)
    dataSlave.append(npm)
    dataSlave.append(nilaiAlpro)
    dataSlave.append(nilaiMatematika)
    dataSlave.append(nilaiAgama)
    dataMaster.append(dataSlave)


def tampilAll():
    os.system('cls')
    if dataMaster == []:
        print("Data Masih Belum Tersedia")
    else:
        print("="*20)
        for j in dataMaster:
            print("Nama :", j[0])
            print("NPM :", j[1])
            print("Nilai Alpro :", j[2])
            print("Nilai Matematika :", j[3])
            print("Nilai Agama :", j[4])
            print("="*20)
        input("Tekan Enter untuk Melanjutkan")


def tampilNPM():
    os.system('cls')
    if dataMaster == []:
        print("Data Masih Belum Tersedia")
    else:
        print("="*20)
        npm = convert_int("Masukan NPM Yang Ingin Dicari Datanya : ")
        for j in dataMaster:
            if j[1] == npm:
                print("="*20)
                print("Nama :", j[0])
                print("NPM :", j[1])
                print("Nilai Alpro :", j[2])
                print("Nilai Matematika :", j[3])
                print("Nilai Agama :", j[4])
                print("="*20)
                break
        else:
            print("NPM Yang Dimasukan Tidak Tersedia")
        input("Tekan Enter untuk Melanjutkan")


def tampilNama():
    os.system('cls')
    if dataMaster == []:
        print("Data Masih Belum Tersedia")
    else:
        print("="*20)
        nama = input("Masukan Nama Yang Ingin Dicari Datanya : ")
        for j in dataMaster:
            if j[0] == nama:
                print("="*20)
                print("Nama :", j[0])
                print("NPM :", j[1])
                print("Nilai Alpro :", j[2])
                print("Nilai Matematika :", j[3])
                print("Nilai Agama :", j[4])
                print("="*20)
                break
        else:
            print("Nama Yang Dimasukan Tidak Tersedia")
        input("Tekan Enter untuk Melanjutkan")


def tampilNilai():
    os.system('cls')
    if dataMaster == []:
        print("Data Masih Belum Tersedia")
    else:
        print("="*20)
        print("1. Nilai Alpro")
        print("2. Nilai Matematika")
        print("3. Nilai Agama")
        pilih = convert_int("Pilih Nilai Yang Ingin Dicari Datanya : ")
        if pilih == 1:
            nama = "Nilai Alpro"
        elif pilih == 2:
            nama = "Nilai Matematika"
        elif pilih == 3:
            nama = "Nilai Agama"
        else:
            return print("Nama Yang Dimasukan Tidak Tersedia")

        for j in dataMaster:
            print("="*20)
            print("Nama :", j[0])
            print("NPM :", j[1])
            print(nama, " :", j[pilih+1])
            print("="*20)
        input("Tekan Enter untuk Melanjutkan")


def cariNPM():
    os.system('cls')
    if dataMaster == []:
        print("Data Masih Belum Tersedia")
    else:
        print("="*20)
        npm = convert_int("Masukan NPM Yang Ingin Dicari Datanya : ")
        for j in dataMaster:
            if j[1] == npm:
                print("="*20)
                print("Nama :", j[0])
                print("NPM :", j[1])
                print("Nilai Alpro :", j[2])
                print("Nilai Matematika :", j[3])
                print("Nilai Agama :", j[4])
                print("="*20)
                break
        else:
            print("NPM Yang Dimasukan Tidak Tersedia")
        input("Tekan Enter untuk Melanjutkan")


def cariNama():
    os.system('cls')
    if dataMaster == []:
        print("Data Masih Belum Tersedia")
    else:
        print("="*20)
        nama = input("Masukan Nama Yang Ingin Dicari Datanya : ")
        for j in dataMaster:
            if j[0] == nama:
                print("="*20)
                print("Nama :", j[0])
                print("NPM :", j[1])
                print("Nilai Alpro :", j[2])
                print("Nilai Matematika :", j[3])
                print("Nilai Agama :", j[4])
                print("="*20)
                break
        else:
            print("Nama Yang Dimasukan Tidak Tersedia")
        input("Tekan Enter untuk Melanjutkan")


def cariNilaiNPM():
    os.system('cls')
    if dataMaster == []:
        print("Data Masih Belum Tersedia")
    else:
        print("="*20)
        npm = convert_int("Masukan NPM Yang Ingin Dicari Datanya : ")
        for j in dataMaster:
            if j[1] == npm:
                print("="*20)
                print("Nama :", j[0])
                print("NPM :", j[1])
                print("Nilai Alpro :", j[2])
                print("Nilai Matematika :", j[3])
                print("Nilai Agama :", j[4])
                print("="*20)
                break
        else:
            print("NPM Yang Dimasukan Tidak Tersedia")
        input("Tekan Enter untuk Melanjutkan")


def deleteNPM():
    os.system('cls')
    if dataMaster == []:
        print("Data Masih Belum Tersedia")
    else:
        print("="*20)
        npm = convert_int("Masukan NPM Yang Ingin Dihapus Datanya : ")
        for j in dataMaster:
            if j[1] == npm:
                dataMaster.remove(j)
                print("Data Berhasil Dihapus")
                break
        else:
            print("NPM Yang Dimasukan Tidak Tersedia")
        input("Tekan Enter untuk Melanjutkan")


def editNama():
    os.system('cls')
    if dataMaster == []:
        print("Data Masih Belum Tersedia")
    else:
        print("="*20)
        nama = input("Masukan Nama Yang Ingin Diedit Datanya : ")
        for j in dataMaster:
            if j[0] == nama:
                print("="*20)
                print("Nama :", j[0])
                print("NPM :", j[1])
                print("Nilai Alpro :", j[2])
                print("Nilai Matematika :", j[3])
                print("Nilai Agama :", j[4])
                print("="*20)
                j[2] = convert_int("Masukan Nilai Alpro Anda : ")
                j[3] = convert_int("Masukan Nilai Matematika Anda : ")
                j[4] = convert_int("Masukan Nilai Agama Anda : ")

                print("Data Berhasil Diubah")
                break
        else:
            print("NPM Yang Dimasukan Tidak Tersedia")
        input("Tekan Enter untuk Melanjutkan")


while True:
    os.system('cls')
    print("="*20)
    print("1. Masukan Input Data")
    print("2. Tampilkan Semua Data")
    print("3. Tampilkan Data Berdasarkan NPM")
    print("4. Tampilkan Data Berdasarkan Nama")
    print("5. Tampilkan Data Nilai")
    print("6. Cari Data Berdasarkan NPM")
    print("7. Cari Data Berdasarkan Nama")
    print("8. Cari Nilai Berdasarkan NPM")
    print("9. Delete Data Berdasarkan NPM")
    print("10. Edit Data Berdasarkan Nama")
    print("11. Exit")
    print("="*20)
    pilihan = input("Pilih Menu Yang Tersedia : ")
    if pilihan == '1':
        inputData()
    elif pilihan == '2':
        tampilAll()
    elif pilihan == '3':
        tampilNPM()
    elif pilihan == '4':
        tampilNama()
    elif pilihan == '5':
        tampilNilai()
    elif pilihan == '6':
        cariNPM()
    elif pilihan == '7':
        cariNama()
    elif pilihan == '8':
        cariNilaiNPM()
    elif pilihan == '9':
        deleteNPM()
    elif pilihan == '10':
        editNama()
    elif pilihan == '11':
        exit()
    else:
        print("Pilihan yang anda pilih tidak tersedia mohon masukan kembali")
