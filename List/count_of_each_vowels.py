# Develop a python program to count the number of each vowel

s = input("Enter the string : ")
s=s.lower()
vowels = "aeiou"
d = {}.fromkeys(vowels,0)
for c in s:
    if c in d:
        d[c] = d[c]+1

for i in d:
    print(i, " = ",d[i])