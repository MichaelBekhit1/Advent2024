##############Testing
# import itertools

# def xmas_check(combinations, iterable, word):
#     local_counter = itertools.count()
    
#     for x_diff, y_diff in combinations:
#         for x, y in zip(local_counter, iterable):
#             if y[local_counter] == word[local_counter]:
#                 next(local_counter)
#                 y += y_diff
#                 x += x_diff
            
        


# combinations = tuple(itertools.product((0, 1, -1), repeat=1))
# print(list(combinations))
# with open("input04.txt","r") as textfile:
#     lines = textfile.read().splitlines()

# counter = itertools.count()
# index_counter = itertools.count()
# word:str = "mas"

# array = zip(counter, lines)

# for x, y in array:
#     starmap = itertools.starmap(xmas_check(combinations), y, word)


#sequence1 = (-1,-1), (0, 0), (1,1)# and reverse
#sequence2 = (-1, 1), (0,0), (-1,1)# and reverse

###########################Solution##################
import itertools
combinations = tuple(itertools.product((1, -1), repeat=2))
# print(list(combinations))
total = 0
# can be a string
xmas = ["M", "A", "S"]

with open("input04.txt","r") as textfile:
    lines = textfile.read().splitlines()
    # "flip the wordsearch" ??? lines = lines[::-1]

# print(lines[0][139])
cols = len(lines)
rows = len(lines[0])
index = 1
index2 = 0
# print(xmas[index+1])
for i in range(cols):
    for j in range(rows):
        y = i
        x = j
        
        # while in bounds and start position == "A"

                   
        if 0 < y < (cols-1) and 0 < x < (rows-1) and lines[y][x] == xmas[index]:

            top_left = lines[y-1][x-1]
            bottom_right = lines[y+1][x+1]
            bottom_left = lines[y+1][x-1]
            top_right = lines[y-1][x+1]

            if top_left == xmas[index -1] and bottom_right == xmas[index+1] and bottom_left == xmas[index-1] and top_right == xmas[index+1]:
                total += 1

            # M  M
            #  A
            # S  S
            elif top_left == xmas[index+1] and bottom_right == xmas[index-1] and bottom_left == xmas[index-1] and top_right == xmas[index+1]:
                total += 1
            # M  S
            #   A
            # M   S

            elif top_left == xmas[index -1] and bottom_right == xmas[index+1] and bottom_left == xmas[index-1] and top_right == xmas[index+1]:
                total +=1
            # S  M
            #  A
            # S M
            elif top_left == xmas[index +1] and bottom_right == xmas[index-1] and bottom_left == xmas[index+1] and top_right == xmas[index-1]:
                total +=1
            # S  S
            #  A
            # M  M

            #output 1472 wrong




            # elif bottom_left == xmas[index-1] and top_right == xmas[index+1]:
                # total +=1
            # elif bottom_left == xmas[::-1][index-1] and top_right == xmas[::-1][index+1]:
                # total +=1


                            





            
# for i in range(cols):
#     for j in range(rows):
  
#         for y_diff, x_diff in combinations:


#             index = 1
#             y = i
#             x = j 
#             # print(x,y)
#             # print(lines[y][x])
#             while  0 <= y < cols and 0 <= x < rows and lines[y][x] == xmas[index]:
                
#                 index+=1
#                 y += y_diff
#                 x += x_diff
#                 # print(x, y) 
#                 # out of bounds check
#                 if 0 <= y < cols and 0 <= x < rows:
#                     if lines[y][x] == xmas[index]:
#                         # print(lines[y][x])
#                         if index == (len(xmas) -1):
#                             total += 1
#                             break

        
        
# # print([combinations for combinations in combination])     
print(total)