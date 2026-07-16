inchar = input("Enter a character: ")
if inchar >= 'A' and inchar <= 'Z':
    print("The character is an uppercase letter" , inchar)
elif inchar >= 'a' and inchar <= 'z':
    print("The character is a lowercase letter" , inchar)
elif inchar >= '0' and inchar <= '9':
    print("You input a number" , inchar)
else:
    print("The character is not a letter." , inchar)