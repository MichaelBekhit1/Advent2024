import itertools
class Guard:
    def __init__(self, grid, current_coords:tuple, next, direction="^"):
        self.current_coords = current_coords
        self.direction = direction
        self.next = next
        self.grid = grid
        next = (current_coords[0], current_coords[(1+1)])



    def turn_90_at_obstacle(self, obstacle):
        if self.next == obstacle:

            if self.direction == "^":
                self.next = (0, 1 )
            # -->    
            elif self.direction == ">":
                self.next = (-1, 0)
            # ¬    
            elif self.direction == "¬":
                self.next = (1, 0)
            # <--   
            elif self.direction == "<":
                self.next = (-1,0)
            # ^    


    def proceed(self, obstacle):
        while #in bounds
            
            if self.next == obstacle:
                self.turn_90_at_obstacle(obstacle)
            else:
                self.grid[self.current_coords] = "X"

                self.current_coords = ((self.current_coords[0]+self.next[0]), (self.current_coords[1]+ self.next[1]))

                if self.direction == "^":
                    self.next = (-1, 0 )
                # ^    
                elif self.direction == ">":
                    self.next = (0, 1)
                # -->    
                elif self.direction == "¬":
                    self.next = (-1, 0)
                # ¬   
                elif self.direction == "<":
                    self.next = (0,-1)
                # <--
        return self.grid


with open("dummy_input06.txt","r") as textfile:
    lines = textfile.read().splitlines()

cols = len(lines)
rows = len(lines[0])

counter = itertools.count()
array = zip(counter,lines)
current_coords = # find "^" index
print(list(array))