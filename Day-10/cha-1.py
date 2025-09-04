#leaf year

year = int(input("Enter a year: "))

def is_leaf_year(year):
    if year % 4==0 and year % 100 !=0 or year % 400==0:
        return True
    else:
        return False

out_put = is_leaf_year(year)
if out_put:
    print(f"{year} is a leaf year")
else:
    print(f"{year} is not a leaf year")