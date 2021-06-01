# Develop a python to write the contents into a file
with open('college.txt','w') as f:
    f.write('RAJALAKSHMI ENGINEERING COLLEGE,\nTHANDALAM,\nCHENNAI,\nTAMILNADU,\nINDIA')

#To check whether the content is written in the file or not
with open('college.txt','r') as f:
    print(f.read())