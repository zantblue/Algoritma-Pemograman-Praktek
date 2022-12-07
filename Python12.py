#Challenge
import numpy as np

data1 = (1,2,3,4,'mizard',"5220411093",5,6,7,8,9,10)
data2 = (11,'18',12,13,14,15,16,17,18,19,20)
a = data1 [0:4]
b = data1 [6:]
c = data2 [0:1]
d = data2 [2:]
genap =[]
ganjil = []
angka1 = a+b
angka2 = c+d
hasil = angka1 + angka2


for i in hasil:
    if i %2 == 0:
        genap.append(i)
    
    else:
        ganjil.append(i)
        
#cekGenap = len(listGenap)  
print("Nama :",data1[4])
print("NIM :",data2[5])
print("umur :",data2[1])
print(len(genap))
print(len(ganjil))
