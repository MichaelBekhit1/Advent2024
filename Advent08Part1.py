import re

nodes = []
with open("input08.txt","r") as textfile:
    lines = textfile.readlines()
    for line in lines:
        line = line.strip()
        x = re.findall("[^\.]", line)
        nodes.append(x)
    
    
for col, row in enumerate(nodes):
    print(col, row)

