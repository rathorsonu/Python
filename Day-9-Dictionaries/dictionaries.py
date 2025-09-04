programing_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}
print(programing_dictionary["Bug"])

programing_dictionary = {}
programing_dictionary["Bug"] = "A moth in your computer."
print(programing_dictionary)

for key in programing_dictionary:
    print(key)
    print(programing_dictionary[key])