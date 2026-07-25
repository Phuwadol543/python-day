score = float(input("Enter your score: "))

while score < 0 or score > 100:
    print('ERROR: The score cannot be less than 0 or greater than 100')
    score = float(input("Enter your score: "))
else: 
    print("Your score is :", score)