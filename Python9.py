import numpy as np

#Membuat array 1 dimensi
# [10 20 30]
dataArray = np.array([10,20,30])
print(dataArray)

#Membuat array multidimensi
dataMulti = np.array(
    [
        [10,20,30],
        [40,50,60]
    ]
)
print(dataMulti)

#Fungsi arange
dataRange = np.arange( 10,50,2)
print(dataRange)

#Fungsi One
dataOne = np.ones([5,6])
print(dataOne)

#Fungsi Identitas
dataIdentitas = np.identity(2)
print(dataIdentitas)

#Fungsi Aritmatika
data1 = np.array([10,'mizard',True])
data2 = np.array([40,50,60])
hasil = data1 * data2
print(hasil)
#print(data1[1])


import numpy as np

data1 = (10,'mizard',20,30,40)
data2 = ('5220411093',50,60,70,80,90)
#data3 = np.array([50,60,70,80,90])
a = np.array([10,20,30,40])
b = np.array([50,60,70,80,90])
hasil = a + b


#Hasil = data2[2], data2[4], data2[5]+data1[0], data2[5]+data1[3] 
#+ data2[1], data2[4], data1[0] + data2[6]
print("Nama :",data1[1])
print("NIM :",data2[0])
print("Result :",hasil)
