# tujuan : untuk memunculkan nama secara acak
import random

nama=["eather","lumine","paimon","mobius"]
bilanganAcak= random.randint(1,3)
print("nama yang muncul : ",nama[bilanganAcak])

# cara lain 
print("Nama yang muncul dengan random choice ",random.choice(nama))