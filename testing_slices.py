test_list = [1,2,3,4,5,6,7]
test_list2 = [5,6,7,8,9,2,3,4,5]
# rule = 4|2
first_rule_index = 3 #3
second_rule_index = 1 #2
# move 3 in front of 2
# test_list = test_list[:second_position]+test_list[first_position:first_position+1]+test_list[second_position:second_position+1]+test_list[first_position+1:]
# to_correct_sequence = to_correct_sequence[:second_position]+to_correct_sequence[first_position:first_position+1]+to_correct_sequence[second_position:second_position+1]+to_correct_sequence[first_position+1:]
# test_list.insert(second_rule_index, test_list[first_rule_index])
# test_list.pop(first_rule_index+1)
# test_list.insert(first_rule_index, test_list[second_rule_index])

print(test_list)



# to_correct_sequence[:first_position+1]+to_correct_sequence[second_position:second_position+1]+to_correct_sequence[second_position+1:]