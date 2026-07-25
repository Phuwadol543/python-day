input_columns = int(input("Enter a column of numbers : "))

for i in range(1,101):
    print(f"{i:3}",end="")
    if i % input_columns == 0:
        print()