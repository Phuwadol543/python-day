Num = 6

def main():
    hours =[0]*Num
    
    for index in range(Num):
        print('Enter the hours wored by employee', \
            index + 1 ,': ' ,sep='', end='')
        hours[index] = float(input())
        
    pay = float(input('Enter the hourly pay rate: '))
    
    for index in range(Num):
        gross_pay = hours[index] * pay
        print('Gross pay for employee', index + 1 ,':$',\
            format(gross_pay,',.2f'), sep='')
        
main()