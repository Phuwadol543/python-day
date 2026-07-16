operation = input("Enter the operation 1.Add , 2.Subtract , 3.Multiply , 4.Divide : ")
num_first = float(input("Enter the first number: "))
num_second = float(input("Enter the second number: "))

if operation == '1':
    result = num_first + num_second
    print("The result of addition is: ", result)
elif operation == '2':
    result = num_first - num_second
    print("The result of subtraction is: ", result)
elif operation == '3':
    result = num_first * num_second
    print("The result of multiplication is: ", result)
elif operation == '4':
    if num_second != 0 and num_first != 0:
        result = num_first / num_second
        print("The result of division is: ", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operation.")