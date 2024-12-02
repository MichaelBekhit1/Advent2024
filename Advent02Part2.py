def safe(record):
    return 
# all(record[i]<record[i+1] for i in range(len(record)-1)) 
# all(record[i]>record[i+1] for i in range(len(record)-1)) and 
# all(abs(record[i]-record[i+1])<3 for i in range(len(record)-1))

    
array = []

# add the records to the array

with open("input02.txt", "r") as textfile:
    for line in textfile.readlines():
        line = line.split()
        for i in range(len(line)):
            line[i]=int(line[i])
        array.append(line)


x = [2,4,5,6]
y = [8,4,2,1]
z = [4, 6, 2, 1]
# print(safe(x),safe(y),safe(z))

total = 0

for record in array:
    if safe(record):
        total +=1

