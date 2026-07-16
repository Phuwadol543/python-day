weight = int(input("You weight in kg?:"))
height = int(input("Your height in cm?:"))
bmi = weight / (height / 100) ** 2
print("Your BMI is: %.2f" % bmi)
