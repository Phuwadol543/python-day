print("KPH\tMPH")
print("-----------------")

for mph in range(60,140,10):
    kph = mph / 0.6214
    print(f'{kph:.2f}\t{mph}')