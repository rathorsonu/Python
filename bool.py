#When you compare two values, the expression is evaluated and python returns the Boolean answer:
print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
	print("b is grater than a")
else:
	print("b is not grater than a")


print(bool("hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))


bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})