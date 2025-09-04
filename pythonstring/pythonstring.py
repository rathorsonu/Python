
print("Hello")
print('Hello')

print("it's alright")
print("he is called 'johnny'")
print('He is called "johnny"')

#Asign a value in veriable
a = "hello"
print(a)


#Multiline String
#you can assign multiple line string to a variable by using three quotes

a = """you can assign multiple line string
to a variable by using three quotes""" 
print(a)

a = '''you can assign multiple line string
to a variable by using three quotes'''
print(a)


a = "Hello Word!"
print(a[0])


for x in "banana":
	print(x)


#String length
#To get the length of a string use the len() function

a = "Hello"
print(len(a))


txt = "The best things in life are free!"
print("free" in txt)


# use it in an if statement:

txt = "The best things in life are free!"
if "free" in txt:
	print("yes 'free' is present" )


#check if not
#To check if a certain phrase or character is not present in a string , we can use the keyword not in.

txt = "The best things in life are free!"
if "expensive" not in txt:
	print("no, 'expensive' is not present")

	