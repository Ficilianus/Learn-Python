age=int(input("masukan umur anda : "))
height= int(input("Masukan tinggi anda : "))

if age >=20 : 
    if height >= 170 :
        print("Biaya masuk Rp.20000")
    elif height <170 :
        print("Tidak boleh masuk")
elif age >= 12 :
    if height >= 170 :
        print("Biaya masuk Rp.10000")
    elif height <170 :
        print("Tidak boleh masuk")
else :
    print("Tidak boleh masuk")