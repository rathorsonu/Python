


print("Welcome to the Love Calculator!\n")
name = input("What is your name? \n")
partner_name = input("What is your partner's name? \n")
def calculate_love_score(girls_name, boys_name):
    combined_name = girls_name + boys_name
    lower_case_name = combined_name.lower()
    t = lower_case_name.count("t")
    r = lower_case_name.count("r")
    u = lower_case_name.count("u")
    e = lower_case_name.count("e")
    first_digit = t + r + u + e

    l = lower_case_name.count("l")
    o = lower_case_name.count("o")
    v = lower_case_name.count("v")
    e = lower_case_name.count("e")
    second_digit = l + o + v + e 

    love_score = int(str(first_digit) + str(second_digit))
    if (love_score < 10) or (love_score > 90):
        print(f"Your love score is {love_score}, you go together like coke and mentos.")
    elif (love_score >= 40) and (love_score <= 50):
        print(f"Your love score is {love_score}, you are alright together.")
    else:
        print(f"Your love score is {love_score}.")

calculate_love_score(name, partner_name)
