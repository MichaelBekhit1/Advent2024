import itertools
import re
class Guard:
    def __init__(self, grid, current_coords:tuple, target_coords:tuple, directions:list[tuple]):
        self.current_coords = current_coords
        self.grid = grid
        self.target_coords = target_coords
        self.directions = directions
        target_coords = ((current_coords[0]+1), current_coords[1])
        

        # merge direction and next tightly-coupled
        # do without symbols
        # remove repitition

    def proceed(self):
        
        # print(self.current_coords)
        # print(self.grid[self.current_coords[0]][self.current_coords[1]])
        # print(self.grid[self.target_coords[0]][self.target_coords[1]])
        directions_index = 0
        #print(self.target_coords[0] + self.directions[directions_index][0])
        while 0 < self.current_coords[0] < cols and 0 < self.current_coords[1] < rows:
            print("x")
            # runs 8 times
            
            if self.grid[self.target_coords[0]][self.target_coords[1]] == "#":
                print("y")
                # loops once more then drops
                self.target_coords=((self.target_coords[0] + self.directions[directions_index][0]),(self.target_coords[1] + self.directions[directions_index][1]))
                
                if directions_index < len(directions):
                    directions_index +=1
                else:
                    directions_index = 0
                
            else:
                
                self.grid[self.current_coords[0]][self.current_coords[1]] = "X"

                self.current_coords = ((self.target_coords[0]), (self.target_coords[1]))
                self.target_coords = ((self.target_coords[0]+self.directions[directions_index][0]), (self.target_coords[1]+self.directions[directions_index][1]))

                
        return self.grid


with open("dummy_input06.txt","r") as textfile:
    lines = textfile.read().splitlines()

cols = len(lines)
rows = len(lines[0])
# directions = ["up", "right", "down", "left"]
directions = [(-1, 0), (0, 1), (1,0), (0,-1)]
# directions_cycle = itertools.cycle(directions)
directions_index = 0
# counter = itertools.count()
array = lines
array_split = []
for line in array:
    line = "!".join(line)
    line = line.split("!")
    array_split.append(line)
    
# print(array_split[6][4])
for col, row in enumerate(array):
    x = re.search("[\^]", row)
    if x:
        current_coords = (col, x.start())
        # print(current_coords)
# get current coords ##########################
#print(current_coords)

target_coords = (7 , 4)
guard = Guard(array_split,current_coords,target_coords, directions)
for col, row in enumerate(guard.proceed()):
    print(col,row)
