score1 = float(input("Enter your score1: "))
score2 = float(input("Enter your score2: "))
score3 = float(input("Enter your score3: "))
avrage = float(score1 + score2 + score3) / 3
print("The average score is: %.2f" % avrage)
if avrage > 95 :
    print("Congratulations!")
