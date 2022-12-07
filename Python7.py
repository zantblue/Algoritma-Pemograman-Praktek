Python 7
    #mencari data berdasarkan nim, nim berdasarkan imputan dari user
dataNIM = int(input("Masukan NIM yang anda cari :"))

data = [
        [500411291, "Faiz"],
        [500411292, "Nazhir"],
        [500411293, "Amrulloh"],
        [500411294, "Reza"],
        [500411295, "Saputra"]
]
        
for i in data:
    if i[0] == dataNIM:
        print(i)
        break
