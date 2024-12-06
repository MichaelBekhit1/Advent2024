# input has 2 parts. 1st contains pairs of numbers. Each pair creates a rule whereby the first must precede the second.
# the second part of the input is a sequence:list[int] and the sequence must be checked against all the rules
# whichever sequences remain must be arranged such that the middle sequence can be selected. The output should be the total of
# the values contained in that middle sequence.
import re

def multiple_index(value, sequence:list):
    matching_indices = []
    
    if str(value) in sequence:
        for i in range(len(sequence)):
            if str(value)==sequence[i]:
                matching_indices.append(i)
    return matching_indices
rules = []
sequences = []
with open("input05.txt","r") as textfile:
    
    lines = textfile.readlines()
    rules = re.findall("(\d\d\|\d\d)", "".join(lines))
    for line in lines[(len(rules)+1):]:
        sequences.append((str(line)).strip())


 
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

        
        if first in sequence and second in sequence:
            first_position = sequence.index(first)
            # print(sequence.index(first))
            indices_of_second = multiple_index(second), sequence
            # print(multiple_index(second,sequence))
            if first_position > min(indices_of_second):
                accepted = False
                
    
    if accepted:
        accepted_sequences.append(sequence)


# print(len(sequences),len(accepted_sequences))
print(len(accepted_sequences))
        


