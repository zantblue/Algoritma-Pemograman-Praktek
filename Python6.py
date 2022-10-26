##penulisan List

##Indexing 
#pemanggilan data bisa menggunakan angka
#         0/-4    1/-3   2/-2   3/-1  
data = ["mizard","udin","ngab","jamal"]
print(data[1])

#Manipulasi list
Insert (Menambahkan nilai berdasarkan index)
data.insert(1,"asep") #Index, nilainnya
print(data)
data.insert(1,"budi")
print(data)

#Append (Menambahkan nilai pada akhir list)
data.append("budi")
data.append("yusup")
data.append("rido")
print(data)

#Extend (Menambahkan list di dalam list)
data_baru = [10,20,30,True]
data.extend(data_baru)
#Mengedit data 
data_ubah = data[1]  = "Biden"
print(data)

#Menghapus data
#remove 
data.remove("rido")
data.remove("udin")

dataAngka = [10,20,40,50,60,30]
#Sort (Mengurutkan dari yang terkecil ke yg terbesar)

#Next : Slicing
dataAngka.sort()
print(dataAngka)

#Reverse (Mengurutkan dari yang terbesar ke yg terkecil)
dataAngka.reverse()
print(dataAngka)

# Slicing (pemotongan)
data = ["mizard","jamal","udin","ngab"]
dataAngka = [10,20,30,40,45]
print(data[1]) Mengambil data list berdasarkan index
SlicingData = data[1:2] #index awal : index setelahnya
SlicingDataAwalSampaiAkhir = data[1:] #Data awal sampai data akhir
SlicingBatasDataAkhir = data[:3] #kasih data sampai akhir
print(data[:3])


#List 2D 
data = [
    ["5220411093","Mizard"],
    ["5220411112","kevina"],
    ["5220411080","Daniel"],
]
print(data)
for i in data:
    print(i[2])

z = 0 
while z < len(data):
    print(data[z][0])
    z = z+1
