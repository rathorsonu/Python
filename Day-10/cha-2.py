def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the line above: ")
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")

while True:
    should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ").lower()
    if should_continue == 'y':
        num3 = int(input("Enter next number: "))
        for number in operations:
            print(number)
            continue
        operation_symbol = input("Pick an operation from the line above: ")
        calculation_function = operations[operation_symbol]
        second_answer = calculation_function(answer, num3)
        print(f"{answer} {operation_symbol} {num3} = {second_answer}")
        answer = second_answer
    else:
        print("Goodbye!")
        break
