def is_armstrong(number):
    Str = str(number)
    total = 0
    for i in range(len(Str)):
        total += int(Str[i]) ** len(Str)
    # if total == number:
    #     return True
    # else:
    #     return False
            
    return total == number


print(is_armstrong(153)) 
print(is_armstrong(123))
print(is_armstrong(9474))
 