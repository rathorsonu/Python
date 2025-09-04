print("welcome to the tip calculator")
bill = float(input("what was the total bill? $"))
tip = int(input("what percentage tip whould ypu like to give ?10,12,15\n"))
people = int(input("how many people to split the bill?"))
tip_as_percent = tip/100
total_tip_ammount = bill*tip_as_percent
total_bil = bill + total_tip_ammount
bill_per_person = total_bil/people
final_amount = round(bill_per_person,2)
print(f"each person shoud pay: ${final_amount}")