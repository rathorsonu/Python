x = 1 #int
y = 2.8 #float
z = 1j #complex

#convert from int to float:
a = float(x)
b = int(y)
c = complex(z)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


#Note: You can not covert complex number to another number
#Random Number - 
#python does not have a random() function to make a random number , but python has a built-in module called random that can used to make random number:

import random
print(random.randrange(10,1000))
