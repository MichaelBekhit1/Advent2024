# start with a list of strings
# if we call the enumerator of the string "columns" and the string itself a "row" then we can imagine that as a 2d list
# there are 8 movements to check and a check has to span the length of xmas. 
# checking starts xmas index at 0. paired with col,row indices depending on movement
# position of each +1, until no match then clear the position vars and proceed from new position in col,row depending on move
# forward iterates across each row checking. backwards iterates backwards across each row checking.
# down iterates through columns checking. up iterates through columns backwards checking
# diagonal is +1col+1row, +1col-1row, -1col+1row, -1col-1row

# more efficient to check from discovery of x than for every char of every string of the array but i figured i'd do that after.




import itertools
total = 0
xmas = ["X", "M", "A", "S"]

with open("input04.txt","r") as textfile:
    lines = textfile.read().splitlines()


cols = len(lines)
rows = len(lines[0])
index = 0
index2 = 0

for i in range(cols):
    for j in range(rows):
        
        # forwards
        if lines[i][j] == xmas[index]:
            index +=1
        
        else:
            index = 0
        
        if index > 2:
            index = 0
            total += 1
        # backwards
        if lines[i][j] == xmas[::-1][index]:
            index +=1
        else:
            index = 0
        if index >2:
            index = 0
            total +=1
        # down
        while index2 < cols:
            if lines[index2][j] == xmas[index]:
                index +=1
                index2+=1
            else:
                index = 0
                index2+=1
            if index > 2:
                index = 0
                total +=1
        index2 = 0
        # wrong
        
dummy_lines = lines[0]
# print(lines[0])
# print(lines[0][::-1][])
print(total)

# 0 1 2 3
# 4 5 6 7
# 8 9 1 2