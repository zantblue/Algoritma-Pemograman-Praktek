##Challenge 2

##Challenge 3
pembeli = input("Masukan jumlah belanja : ")
pembeli = int(pembeli)
if pembeli >= 100000:
    diskon = 10/100
else :
    diskon = 5/100
hitung = pembeli * diskon
total = pembeli - hitung
print("diskon :",hitung)
print("harga setelah diskon :", total)
