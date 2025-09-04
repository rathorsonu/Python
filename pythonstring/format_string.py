#String Format

#As we learned in the python variables chapter, we cannot combine strings and numbers like this:

#age =  36
#txt = "My name is john, I am" + age
#print(txt)

#TypeError: can only concatenate str (not "int") to str


#but we can combine strings and number by f-strings or the formate() method

#F-strings
#F-String was introduced in python 3.6 and is now the prefered way of formatting strings.
#To specify a string as an f-string , simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other oprations.

age = 36 
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)


price = 59
txt = f"The price is {price: 2f} dollars"
print(txt)

