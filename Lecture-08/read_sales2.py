with open('Lecture-08/sales.txt','r') as sales_file:
    for line in sales_file:
        amonut = float(line)
        print(format(amonut,'.2f'))