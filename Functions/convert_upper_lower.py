# Convert the given string into upper and lower case using python function

def conv_upper_lower(string):
    return string.upper(),string.lower()

s =input("Enter the string : ")
upper,lower = conv_upper_lower(s)
print("Uppercse : ",upper)
print("Lowercase : ",lower)