# return total number of "safe" records. A record is a line in the input containing integers separated by spaces. A record is
# safe if is in ascending or descending order of value and the difference between each consecutive integer is less than 3

def is_ascending(record: list[int]) -> bool:
        
    loop_length = len(record) -1

    for i in range(loop_length):
        if record[i]>= record[(i+1)]:
            return False
    return True
def is_descending(record: list[int]) -> bool:
    loop_length = len(record) -1

    for i in range(loop_length):
        if record[i]<= record[(i+1)]:
            return False
    return True
def is_safe_difference(record: list[int]) -> bool:
    loop_length = len(record) -1

    for i in range(loop_length):
        if abs(record[i] - record[(i+1)])>3:
            
            return False
    return True

def total_safe_records(input_array: list[list]) -> int:
    total_safe_records = 0
    for record in input_array:
        
        if (is_ascending(record) or is_descending(record)) and is_safe_difference(record):
            total_safe_records += 1
    return total_safe_records


dummy_record_asc_safe = [14, 16, 18, 20]
dummy_record_desc_safe = [18, 16, 14]
dummy_record_asc_unsafe = [1, 5, 6, 8]
array = []

# add the records to the array

with open("input02.txt", "r") as textfile:
    for line in textfile.readlines():
        line = line.split()
        for i in range(len(line)):
            line[i]=int(line[i])
        print(line)


#print(array, total_safe_records(array))


        