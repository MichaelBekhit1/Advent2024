import re


class Node:
    def __init__(self,col,row_position,value):
        self.col = col
        self.row_position = row_position
        self.value = value
        
nodes = []

with open("input08.txt","r") as textfile:
    lines = textfile.readlines()
    for count, line in enumerate(lines):
        line = line.strip()
        x = re.findall("[^\.]", line)
        for node in x:
            node_row_position = line.index(node)
            node_value = node
            node = Node(count, node_row_position, node_value)
            nodes.append(node)


        
        lines[count] = line

# nodes is a list of Node objects

node_values = []


for node in nodes:
    if (node.value in node_values) == False:
        node_values.append(node.value)

def recursive_function(node_value_index):
    
    recursive_function(node_value_index - 1)

# describe the recursion
#-----------------------------------#

# checking all the values in a row is like checking the first and then all the values in a row

# paired_positions = []

# for node, node_value in zip(nodes, node_values):
    # if node.value == node_value:
        # paired_positions.append((node.col, node.row_position, node_value))


# print(paired_positions)
# output:

# ['C', 'e', '7', 'O', 'z', 't', 'k', 'h', '9', '5', 'T', 'o', 'c', 'H', 'w', '3', 'B', '6', 's', '4', '8', 'b', 'X', '1', 'J', 'K', 'x', '2', '0', 'j', 'W', 'G', 'E', 'S', 'Z', 'g']
# [[(1, 33, 'C'), (2, 1, 'e'), (2, 12, '7'), (2, 13, 'O'), (3, 37, 'z'), (4, 22, 't')]]

# why does this terminate without completing the sequence of node values

# I know that if the lists are different lengths then zip ends prematurely but that doesnt seem to be the case here?

###########################testing########################

letters = ["a","b","c"]
numbers = [10,20,30, 15, 20, 40]
largest_number = 0

for letter,number in zip(letters,numbers):
    print(letter,number)
    if number > largest_number:
        largest_number = number

## output = 30
tup = (1,2,3)
print(largest_number)