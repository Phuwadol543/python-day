def calculate_stats(number):
    total_sum = sum(number)
    average = total_sum / len(number)
    maxnum = max(number)
    minnum = min(number)
    return total_sum , average , maxnum , minnum

numbers = [5,10,15,25,25]
total , avg , max_num , min_num = calculate_stats(numbers)
print(f'Total Sum: {total}\nAverage: {avg}\nMaximum: {max_num}\nMinimum: {min_num}')