# input has 2 parts. 1st contains pairs of numbers. Each pair creates a rule whereby the first must precede the second.
# the second part of the input is a sequence:list[int] and the sequence must be checked against all the rules
# whichever sequences remain must have their middlemost value totalled
import re

def multiple_index(value, sequence:list):
    matching_indices = []
    
    if value in sequence:
        for i in range(len(sequence)):
            if value==sequence[i]:
                matching_indices.append(i)
    return matching_indices
rules = []
sequences = []
with open("input05.txt","r") as textfile:
    
    lines = textfile.readlines()
    rules = re.findall("(\d\d\|\d\d)", "".join(lines))
    for line in lines[(len(rules)+1):]:
        line = (str(line)).strip()
        line = line.split(",")
        for value in line:
            value = int(value)
        sequences.append(line)
        


 
# output for rules and sequences appears as expected
rules_tuples = []
for rule in rules:
    rule = rule.split("|")
    rules_tuples.append((rule[0],rule[1]))

# print(rules_tuples)
test_sequence = sequences[0]
test_sequence2 = ["57", "60","57", "60", "60"]
# ['57,47,82,32,18']
accepted_sequences = []
rules = []



for sequence in sequences:
    # print(sequence)
    accepted = True
    for first,second in rules_tuples:
        # print(first)

        
        if first in sequence and second in sequence:
            # print("x")
            first_position = sequence.index(first)
            # print(sequence.index(first))
            indices_of_second = multiple_index(second, sequence)
            # print(multiple_index(second,sequence))
            if first_position > min(indices_of_second):
                accepted = False
                
    
    if accepted:
        accepted_sequences.append(sequence)


# print(len(sequences),len(accepted_sequences))
total = 0
for accepted_sequence in accepted_sequences:
    mid = int(len(accepted_sequence)*0.5)
    total+= int(accepted_sequence[mid])

        
print(sequences)
print(total)

