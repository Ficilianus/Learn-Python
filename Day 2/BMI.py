# The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. This is the formula used to calculate it:
# bmi is equal to the person's weight divided by the person's height squared.


height = 1.65
weight = 84
# cara 1 untuk pangkat 2
bmi =weight/(height*height)
print("hasil" , bmi)
#cara 2 untuk pogkat 2
bmi=weight/(height**2)
print("hasil" , bmi)

# lalu jika ingin melakukan pembulatan maka tambhakan round()
print("hasil",round(bmi))
# dan jika ingin melakukan pembulatan 2 angka di belakang nol maka tambahkan ,2
print("hasil", round(bmi, 2))