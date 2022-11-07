beli = []
barang =[]
diskon=k=total=diskon_tambah=jmlh_brg = 0 
def convert_int(text):
    try:
        var = int(input(text))
    except:
        print("Hanya Masukan Angka Saja")
    return var
def admin():
    global diskon
    print("Menu")
    print("[1] Input Barang")
    print("[2] Input Diskon Barang")
    pilih = convert_int("Pilih Menu :")
    if pilih == 1:
        kode_barang = input("Masukan kode barang :")
        nama_barang = input("Masukan nama barang :")
        harga_barang = convert_int("Masukan harga barang :")
        barang.append([kode_barang,nama_barang,harga_barang])
    elif pilih == 2:
        diskon = convert_int("Masukan diskon barang :")
        
def pelanggan():
    print("Menu")
    print("[1] Lihat Data Barang")
    print("[2] Input Barang")
    print("[3] Bayar")
    pilih = convert_int("Pilih Menu :")
    if barang != []:
        if pilih == 1:
            for j in barang:
                print("Kode Barang : ",j[0])
                print("Nama Barang : ",j[1])
                print("Harga Barang : ",j[2])
        elif pilih == 2:
            ulang = True
            while ulang:
                kode_beli = input("Masukan Kode Barang yang ingin dibeli :")
                for j in barang:
                    if j[0] == kode_beli:
                        qty = convert_int("Masukan Jumlah barang yang dibeli :")
                        tmp = j.copy()
                        tmp.append(qty)
                        beli.append(tmp)
                        lagi = input("Apakah ingin membeli lagi ? [y/n]")
                        if lagi == 'y':
                            break
                        elif lagi == 'n':
                            ulang = False
                            break
                else:
                    print("Barang tidak ditemukan")
                    break
        elif pilih == 3:
            global k,total,diskon_tambah,jmlh_brg
            print("Struk Belanja".center(20,'='))
            print("Barang yang dibeli :")
            for j in beli:
                k+=1
                print(k," Kode Barang   : ",j[0])
                print("   Nama Barang   : ",j[1])
                print("   Harga Barang  : ",j[2])
                print("   Qty Barang    : ",j[3])
                total += j[2] * j[3]
                jmlh_brg += j[3]
            if jmlh_brg > 10:
                diskon_tambah = 20000
            elif jmlh_brg > 5:
                diskon_tambah = 10000
            print("Harga total      :",total)
            print("Diskon           :",diskon)
            print("Diskon tambahan  :",diskon_tambah)
            print("Total Bayar      :",total - diskon - diskon_tambah)
    else:
        print("Data Belum Tersedia")

while True:
    # print(barang)
    # print(beli)
    print("Pilih User :")
    print("[1] Admin")
    print("[2] Pelanggan")
    print("[3] Exit")
    pilihan = convert_int("Pilih User : ")
    if pilihan == 1:
        admin()
    elif pilihan == 2:
        pelanggan()
    elif pilihan == 3:
        exit
