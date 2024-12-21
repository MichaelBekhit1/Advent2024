import re
import itertools

# for every sequence, 

rules:list[tuple] = []
sequences:list[list] = []

with open("input05.txt","r") as textfile:
    
    lines = textfile.readlines()
    for line in lines:
        regex = re.findall("(\d\d)\|(\d\d)", line)
        if regex:
           rules.append(regex[0])
           # this just skips the empty first line
    for line in lines[len(rules)+1::]:
        sequences.append(line.strip().split(","))
        
                    
incorrect_sequences = []
for sequence in sequences:
    # sequence is list[str]
    correct = True
    
    for rule in rules:
        # rule:tuple
        if rule[0] in sequence and rule[1] in sequence:
            # if both the first and second values are in the sequence, if the position in the sequence of the first is after the position in the 
            # sequence of the second then that is not correct
            if sequence.index(rule[0]) > sequence.index(rule[1]):
                correct = False
    if correct == False:
        #if the sequence is not correctly ordered, put it in the incorrect sequence list
        incorrect_sequences.append(sequence)
# incorrect sequences is list[list[str]]
corrected_sequences = []
for incorrect_sequence in incorrect_sequences:
    
    # incorrect sequence is list[str]
    
    changed = True
    # to_correct_sequence = incorrect_sequence.copy()
    while changed:
        for rule in rules:

            
            
            
                # end the loop unless correction sequence runs
                changed = False
                # correction sequence runs if both parts of the rule are present in the sequence and the index for the first is larger than the index for the
                # second
                if rule[0] in incorrect_sequence and rule[1] in incorrect_sequence:
                    
                    if incorrect_sequence.index(rule[0]) > incorrect_sequence.index(rule[1]):
                        # if correction sequence has run, reactivate while loop
                        changed = True

                        first_rule_index = incorrect_sequence.index(rule[0])
                        second_rule_index = incorrect_sequence.index(rule[1])
                        # this moves the second position to immediately before the first and captures the rest of the data in order
                        # I checked this output in testing_slices.py
                        incorrect_sequence.insert(second_rule_index, incorrect_sequence.pop(first_rule_index))
                        
            
    corrected_sequences.append(incorrect_sequence)
total = 0 
# corrected_sequences:list[list[str]]                   
for corrected_sequence in corrected_sequences:
    # corrected_sequence: list[str]
    length_of_sequence = len(corrected_sequence)
    
    middle = (length_of_sequence-1)/2
    
    value =  corrected_sequence[int(middle)]
    print(corrected_sequence, middle,value)
    total += int(value)

print(total) 
# print(len(rules))
# print(sequences)
# 6190
# 6424


