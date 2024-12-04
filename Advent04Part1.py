# establish the data in a grid or multidimensional array or a format that retains its shape(rows,cols)
# apply word search logic for "xmas" - top to bottom, bottom to top, left to right, right to left, diagonally from top right
# to bottom left, diagonally from bottom left to top right, diagonally from top left to bottom right, diagonally from bottom
# right to top left for a total of 8 valid moves

# first thought: if it were arranged in a multidimensional array wherein each list was a row and the position in the array
# represented columns then from each point in the row, I could run logic for valid moves and if it completes, apply a credit
# to the total. Each logic would have to entail out of bounds checks so there would be loop management or stepped iteration.
import re

class Solution:
    def __init__(self,data_array, start_position, total=0) -> None:
        self.start_position = start_position
        self.data_array = data_array
        self.total = total
        
   

    def cols(self):
        cols = len(self.data_array)
        return cols      

    def rows(self):
        # assumes every row same length
        rows = len(self.data_array[0])
        return rows
    
    def in_bounds(self,position):
        if position[0]>=0 and position[0]<= self.cols() and position[1]>=0 and position[1]<=self.rows():
            return True
        else:
            return False





    
    def down(self,col):
        pass

         
    def up(self,col):
        pass

    def left(self,row):
        row = row[::-1]
        row_iter = iter(row)

        if next(row_iter) == "X":
            if next(row_iter) == "M":
                if next(row_iter) == "A":
                    if next(row_iter) == "S":
                        return True
        return False

    def right(self, row):
        
        row_iter = iter(row)

        if next(row_iter) == "X":
            if next(row_iter) == "M":
                if next(row_iter) == "A":
                    if next(row_iter) == "S":
                        return True
        return False

    def diag_top_left_to_bottom_right(self):
        pass

    def diag_bottom_right_to_top_left(self):
        pass

    def diag_bottom_left_to_top_right(self):
        pass

    def diag_top_right_to_bottom_left(self):
        pass


    def output_total(self):
        # for each value in each row, position=start_position, run all movement methods and for each complete total +=1
        return self.total

data = [["X","M","A","S","X","M","A","S"],["X","M","S","A"],["D","O","G"]]
start_position = [0,0]
solution = Solution(data, start_position)

col = -1
with open("input04.txt","r") as textfile:
    lines = textfile.readlines()
    for line in lines:
        
        x_start_positions = []
        for row_position, value in enumerate(line):
            if value=="X":
                x_start_positions.append(row_position)
        col +=1

        # print(x.start())
        changed = True
        total = 0

        while changed == True:
            starting_total = total
            # row only checks
            for start_position in x_start_positions:
                if solution.in_bounds(col, start_position):

                    if solution.right(data[start_position]):
                        total+=1
                    if solution.left(data[start_position]):
                        total +=1
    #if solution.up(data[x.start()]):
    #    total+=1
    #if solution.down(data[x.start()]):
    #    total+=1
    #if solution.diag_bottom_left_to_top_right(data[x.start()]):
    #    total+=1
    #if solution.diag_bottom_right_to_top_left(data[x.start()]):
    #    total+=1
    #if solution.diag_top_left_to_bottom_right(data[x.start()]):
    #    total+=1
    #if solution.diag_top_right_to_bottom_left(data[x.start()]):
    #    total+=1
    if starting_total != total:
        changed = False

print(total)

# print(data[0][::-1])
    



print(start_positions)