keepgoing = 'y'


while keepgoing.upper() == 'Y' or keepgoing.upper() == 'YES':
    sales = float(input("Enter the sales amount of sales: "))
    commission = float(input("Enter the commission rate: "))
    total = sales * commission
    print(f'the commission is: {total:.2f}')
    keepgoing = input('Do you want to calculate another  ' +  'commission (Enter y for yes): ')