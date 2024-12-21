test_list2 = [1,2,3,4]
test_list = [5,6,7,8]
first_position = 2 #3
second_position = 1 #2
# move 3 in front of 2
test_list = test_list[:second_position]+test_list[first_position:first_position+1]+test_list[second_position:second_position+1]+test_list[first_position+1:]
# to_correct_sequence = to_correct_sequence[:second_position]+to_correct_sequence[first_position:first_position+1]+to_correct_sequence[second_position:second_position+1]+to_correct_sequence[first_position+1:]
print(test_list)

# to_correct_sequence[:first_position+1]+to_correct_sequence[second_position:second_position+1]+to_correct_sequence[second_position+1:]