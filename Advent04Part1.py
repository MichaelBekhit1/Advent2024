# establish the data in a grid or multidimensional array or a format that retains its shape(rows,cols)
# apply word search logic for "xmas" - top to bottom, bottom to top, left to right, right to left, diagonally from top right
# to bottom left, diagonally from bottom left to top right, diagonally from top left to bottom right, diagonally from bottom
# right to top left for a total of 8 valid moves

# first thought: if it were arranged in a multidimensional array wherein each list was a row and the position in the array
# represented columns then from each point in the row, I could run logic for valid moves and if it completes, apply a credit
# to the total. Each logic would have to entail out of bounds checks so there would be loop management or stepped iteration.
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