PIN = input("Masukan PIN : ")
riwayat = []
def Konfirmasi(noRek,Nominal):
    yakin = input("Apakah ada yakin?[y/t] ")
    for i in range(2):
        if yakin == "y":
            inputPIN = input("masukan PIN anda : ")
            if inputPIN == PIN: 
                riwayat.append(noRek)
                riwayat.append(Nominal)
                print("TRANSAKSI BERHASIL")
                break
            else : print("PIN SALAH")
        elif yakin == "t":
            print("TRANSAKSI DIBATALKAN")
            break
def tranfer():
    InputNoRek = input("Masukan Nomer Rekening : ")
    InputNominal = input("Masukkan Nominal : ")
    Konfirmasi(InputNoRek,InputNominal)


while True:
    print("="*20)
    print("Menu ")
    print("1. Transfer")
    print("2. Riwayat Transaksi")
    print("3. Tarik Tunai")
    print("4. Exit")
    print("="*20)
    InputMenu = input("Pilih menu :")
    if InputMenu == "1":
        tranfer()
    elif InputMenu == "2":
        print(riwayat)
