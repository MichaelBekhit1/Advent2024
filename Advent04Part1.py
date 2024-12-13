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
combinations = itertools.product((0, 1, -1), repeat=2)
total = 0
xmas = ["X", "M", "A", "S"]

with open("input_dummy.txt","r") as textfile:
    lines = textfile.read().splitlines()


cols = len(lines)
rows = len(lines[0])
index = 0
index2 = 0

# for i in range(cols):
#     for j in range(rows):
#         index = 0
#         if lines[i][j] == xmas[index]:
#             index+=1
#             next_i = i+1
#             next_j = j-1
#             # out of bounds check
#             if 0 <= next_i < cols and 0 <= next_j < rows:
#                 if lines[next_i][next_j] == xmas[index]:
#                     print(lines[next_i][next_j])

            
            
for i in range(cols):
    for j in range(rows):
        for combination in combinations:
            # print(combination[0])
            if combination == (0,0):
                continue

            y_diff = combination[0]
            x_diff = combination[1]
            print(x_diff, y_diff)

            index = 0
            y = i
            x = j 
            print(lines[y][x])
            while  0 <= y < cols and 0 <= x < rows and lines[y][x] == xmas[index]:
                
                index+=1
                y += y_diff
                x += x_diff
                print(x, y) 
                # out of bounds check
                if 0 <= y < cols and 0 <= x < rows:
                    if lines[y][x] == xmas[index]:
                        print(lines[y][x])
                        if index == 3:
                            total += 1
                            break

        
        
# print([combinations for combinations in combination])     
print(total)

# 0 1 2 3
# 4 5 6 7
# 8 9 1 2

