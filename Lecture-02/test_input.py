# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# print("Hello " + first_name + " " + last_name + "!")

name = input("what is your name?")
age = int(input("what is your age?"))
income = float(input("what is your income?"))

print("Here is the Data you entered:")
print("Name:", name)
print("Age:", age)
print("Income:", format(income, '12,.2f'))