def print_all(*args):
    for i, arg in enumerate(args):
        print(f'Argument {i + 1}: {arg}')
        
print_all('Python', 15, 3.8, True , [1,2,3],{'key':'value'})