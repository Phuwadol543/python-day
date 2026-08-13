number = [4,2,9,1,5,6]

leng = len(number)
print(f"Length of the list: {leng}")

total = sum(number)
print(f'Sum : {total}')

max = max(number)
print(f"Max: {max}")

min = min(number)
print(f"Min: {min}")

sort_number = sorted(number)
print(f"Sorted: {sort_number}")

bool_list = [False,True,False]
any_true = any(bool_list)
print(f"Is any element True? {any_true}")

all_true = all(bool_list)
print(f"Are all element True? {all_true}")

string = "hello"
char_list = list(string)
print(f"List of characters: {char_list}")

reversed_number = list(reversed(number))
print(f"Recersd list: {reversed_number}")

enumerate_number = list(enumerate(number))
print(f"Enumeraated list: {enumerate_number}")