def find_max(*arge):
    if not arge:
        return None
    max_value = arge[0]
    for number in arge:
        if number > max_value:
            max_value = number
    return max_value

print(f'the maximum value is: {find_max(3,5,7,2,8)}')

print(f'the maximum value is: {find_max()}')