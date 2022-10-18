#Perulangan For 

#for nilai in sequence:
#   blok code

#Contoh 1
for i in "mizard":
    print(i)

#Contoh 2 Menggunakan fungsi range()
for i in range(10): #Start(dimulai dari 0 dan berhenti diangka sebelum angka terakhir)
    print(i)
for i in range(2,11): #Stop(berhenti diangka sebelumnya angka terakhir)
    print(i)
for i in range(5,20,2): #Step(bertambah sejumlah angka yang diisikan)
    print(i)

#Contoh 3 perulangan menggunakan continue
for i in range(10):
    print(i)
    if i == 5:
        print(i)
        continue

#Contoh 4 perulangan menggunakan break
for i in range(20):
   if i == 15:
        print("Ini perulangan ke-",i)
        break 

#Contoh 5 perulangan menggunakan list
data = ["mizard","Jamal","Udin","Ngab"]
for i in data:
    if i == "Udin":
        print(i)
        break

#Perulangan while
#while nilai operator sequence:
#   blok kode

#Contoh 1
i = 2
while i < 11:
    print(i)
    i += 1

#Contoh 2
data = [10,20,30,40]
for i in data:
    if i == 30:
        print(i)
        break
i = 1 
while i < len(data):
    if data[i] == 30:
      print(data[i])
      break
    i += 1
    
    
#Challenge
for i in range(2,41):
    if i == 10:
        print("ini adalah nilai",i)
        continue
    elif i == 20:
        print("ini adalah nilai",i)
        continue
    elif i == 30:
        print("ini adalah nilai",i)
        break
