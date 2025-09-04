import random

#random_number = random.random()
#print(random_number)
#random_number = random.randint(1,10)
#print(random_number)

#Note: randrange() is also used to make random number within a range but it does not include the last number
random_number = random.randint(0,1)
if random_number==0:
    print("Tails")
else:
    print("Heads")
    