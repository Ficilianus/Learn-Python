print("welcome")

size=input("what size pizza do you want ? s, m, l ? ")
pappronoi=input("do you want papproni ? y or n ? ")
extra_chesse=input("do you want extra chesee ? y or n ")
bill=0
if size == "s":
    bill+=10000
    if pappronoi =="y": 
        bill+=2000
    if extra_chesse =="y": 
        bill+=3000
elif size == "m":
    bill+=20000
    if pappronoi =="y": 
        bill+=5000
    if extra_chesse =="y": 
        bill+=5000
elif size=="l" :
    bill=30000
    if pappronoi =="y": 
        bill+=2000
    if extra_chesse =="y": 
        bill+=8000
else :
    print("error")

print("total : ",bill)