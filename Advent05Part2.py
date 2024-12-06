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
            indices_of_second.sort(reverse=True)
            values_to_append = []
            if first_position > min(indices_of_second):
                accepted = True

                for index in indices_of_second:
                    values_to_append.append(sequence[index])
                    sequence.pop(index)
                if values_to_append:
                    for value in values_to_append:
                        sequence.append(value)
                    
            
    if accepted:
        accepted_sequences.append(sequence)

       
            

            # store them, remove them from the list from the highest first, add them to the end

        

            
            

                    
    

                
    
    


# print(len(sequences),len(accepted_sequences))
total = 0
for accepted_sequence in accepted_sequences:
    mid = int(len(accepted_sequence)*0.5)
    total+= int(accepted_sequence[mid])

        
# print(sequences)

print(total)