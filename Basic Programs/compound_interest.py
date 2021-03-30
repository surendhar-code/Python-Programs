principle=int(input("Enter the principle amount value : "))
rate=float(input("Enter the rate of interest value : "))
time_period=int(input("Enter the time_period : "))
amount=principle*(pow((1+rate/100),time_period))
CI=amount-principle
print("The compound interest is : ",CI)

