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
dataAngka.sort()
print(dataAngka)
#Reverse (Mengurutkan dari yang terbesar ke yg terkecil)
dataAngka.reverse()
print(dataAngka)
