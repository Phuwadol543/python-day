hours_worked = float(input("Enter the number of hours worked: "))
pay_rate = float(input("Enter the pay rate: "))

if hours_worked <= 40:
    gross_pay = hours_worked * pay_rate
    print("Gross pay is: %.2f" % gross_pay)
else:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * pay_rate * 1.5
    gross_pay = (40 * pay_rate) + overtime_pay
    print("Gross pay is: %.2f" % gross_pay)