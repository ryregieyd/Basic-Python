x = float(input("Input Nominal: "))
if x >= 100000:
    total = x * 0.10
    print("Total Payment: ", x - total)
else:
    total = x
    print("no discount", "Total Payment: ", total)
    

