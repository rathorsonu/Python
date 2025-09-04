print("welcome to Python Pizza deliveries!")
size = input("what size pizza do you want? S, M Or L:\n")
pepperoni = input("Do you want pepperoni on your pizza? y or N:\n")
extra_cheese = input("Do you want extra cheese? Y or N:\n")
bill = 0
if size.upper() == "S":
    bill += 15
elif size.upper() == "M":
    bill += 20
elif size.upper() == "L":
    bill += 25
else:
    print("invalid input")

if pepperoni.upper() == "Y":
    if size.upper() == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese.upper() == "Y":
    bill += 1


print(f"your final bill is: ${bill}")
