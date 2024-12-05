# input contains pairs of numbers. Each pair creates a rule whereby the first must precede the second.
# the second part of the input is a sequence and the sequence must be checked against all the rules
# whichever sequences remain must be arranged such that the middle sequence can be selected. The output should be the total of
# the values contained in that middle sequence.
import re

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
# ['57,47,82,32,18']
accepted_sequences = []
rules = []
accepted = True

# process for single sequence


for first,second in rules_tuples:

    if second == "57":
        print(first)
    if first in test_sequence and second in test_sequence:
        if test_sequence.index(first) > test_sequence.index(second):
            accepted = False
    
if accepted:
    accepted_sequences.append(test_sequence)

print(accepted_sequences)


        



        


