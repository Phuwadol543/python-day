input_row = int(input("Enter a row of numbers : "))
input_columns = int(input("Enter a column of numbers : "))

for i in range(input_row):
    for j in range(input_columns):
        print('*', end=' ')
    print()
