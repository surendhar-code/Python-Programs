# evelop a Python program to append the contents into an existing file.
with open('college.txt','a') as f:
    f.write("\nAdmissions are open for this year...")


# Display the contents in the file
with open('college.txt','r') as f:
    print(f.read())

