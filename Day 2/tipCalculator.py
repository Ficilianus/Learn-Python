# projek untuk membuat menghitung total tip

print("welcome to the tip calculator")
bill=float(input("what was the total bill ? Rp."))
tip=int(input("what precantance tip would you like to give? 10 12 15 ? : "))
pepole =int(input("How many people to split the bill? "))
tip_percantance = tip/ 100
total_tip_ammout=bill * tip_percantance
total_bill = bill + total_tip_ammout
bill_per_person= total_bill/pepole
final_amont = round(bill_per_person,2)
print(f"Each person should pay : Rp.{final_amont}")