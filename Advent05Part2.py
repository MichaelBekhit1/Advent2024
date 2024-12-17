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
    for line in lines[len(rules)+1::]:
        sequences.append(line.strip().split(","))
        
                    
# for each sequence, every value appearing in the second position in the rules list should appear after the value in the first position, if that is also
# in the sequence.
# if both parts in sequence, part 1 index should be before part 2 index
# A B C D if B before D and D before A then D A B C, C D A B.
# while...if changed.

incorrect_sequences = []
for sequence in sequences:
    # print(sequence)
    correct = True
    
    for rule in rules:
        if rule[0] in sequence and rule[1] in sequence:
            if sequence.index(rule[0]) > sequence.index(rule[1]):
                correct = False
    if correct == False:
        incorrect_sequences.append(sequence)

corrected_sequences = []
for incorrect_sequence in incorrect_sequences:
    
    # print(incorrect_sequence)
    
    changed = True
    

    for rule in rules:
        to_correct_sequence = incorrect_sequence.copy()
        while changed:
            changed = False
            if rule[0] in to_correct_sequence and rule[1] in to_correct_sequence:
                
                if to_correct_sequence.index(rule[0]) > to_correct_sequence.index(rule[1]):
                    changed = True
                    first_position = to_correct_sequence.index(rule[0])
                    second_position = to_correct_sequence.index(rule[1])
                    to_correct_sequence = to_correct_sequence[:second_position]+to_correct_sequence[first_position:first_position+1]+to_correct_sequence[second_position:second_position+1]+to_correct_sequence[first_position+1:]
                    
        
    corrected_sequences.append(to_correct_sequence)
total = 0                    
for corrected_sequence in corrected_sequences:
    middle = int(len(corrected_sequence) * 0.5)
    total+= int(corrected_sequence[middle])

print(total) 

# 6190 wrong
