units = int(input("Enter the units consumed : "))
if units <= 100:
    amount = units*3.00
elif units <=200:
    amount = 3.25*units
elif units <= 500:
    amount = 700.00 + 4.60 * (units - 200)
else:
    amount = 2080.00 + 6.60 * (units - 500)

print("Units = ",units, " Amount : ",amount)