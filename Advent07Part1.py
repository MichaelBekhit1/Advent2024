# learning goals: recursion. itertools
# input e.g. 190: 19 10 In this example there is one space for an operator - between 19 and 10. The first number is the total
# if there is an operator or operators that resolve the seond series to equate to the first number then the sequence is valid
# return the grand total of the totals of the valid sequences
import re
import operator


with open("input07.txt","r") as textfile:
    lines = textfile.readlines() # a list of strings

total_pattern = re.compile("(\d+):")
operand_pattern = re.compile(" (\d+)")
totals = []
operands = [] # array of lists of operands:str
for line in lines:
    totals.append(total_pattern.findall(line))
    operands.append(operand_pattern.findall(line))

for operand_list in operands:
    for i in range(len(operand_list)):
        operand_list[i] = int(operand_list[i])

# operands is now an array of lists of operands:int
grand_total = 0


for i in range(len(operands)): # iterate through sequences
    total = int(totals[i][0]) # input total for given sequence
    operand_sequence = operands[i] # operands for given sequence
    accepted = False
    # each sequence now has total:int, operand_sequence:list[int],accepted:bool=False
    operand_total = 0

    
    # sequence  = ["1","2","3"]
    # resolve as 1*2*3,1+2+3,1+2*3,1*2+3
    ptr = 0
    ptr2 = 1
    outcomes = []

    for j in range(len(operand_sequence)):
        ptr = operator.add(operand_sequence[j],ptr)
        ptr2 = operator.mul(ptr2, operand_sequence[j])

        
    for outcome in outcomes:
        if outcome == total:
            accepted = True

    
    



        
        
            
    
    
    if accepted:
        grand_total+=total # if accepted, add the sequence's input total to the grand total




    




    

        
    


test_sequences = [lines[0], lines[1], lines[2]]


