# copy content of one file into another file
# create input.txt file
f1 = open('input.txt','w')
f1.write("Welcome to\nREC CSBS\nThandalam")
f1.close()
# create output.txt file
f2 = open('output.txt','w')
f1 = open('input.txt','r')
# copying
for line in f1:
    f2.write(line)
f1.close()
f2.close()
# Displaying contents of the output.txt file
f1 = open('output.txt','r')
output_contents = f1.read()
print(output_contents)
f1.close()
