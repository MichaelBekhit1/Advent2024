# when a report is A: 1, B:4, C:5, D:7
# C could be removed or D could be removed to make it a safe record
# at the point of error, it creates a possible 3 values to remove. If problem is at C, the removal could either be B, C or D so I need to check
# the record without B, C D and if either is safe then the sequence can be made safe.

# new record = record without B. check. if still unsafe
# new record = record without C. check. if still unsafe
# new record = record without D

# return problem index or True        
def safe(record):
    for i in range(len(record)):
        record[i] = int(record[i])
    index = 0
    desc_problem_index = None
    asc_problem_index = None
    desc = True # made false if a single value is not descending
    asc = True # made false if a single value is not ascending
    for i in range(len(record)):
        
        if 0 < i <= len(record):
            
            difference = abs(record[i] - record[index])
            if difference > 3:
                
                print("diff")
                return i
        # if in bounds    
        if 0 < i <= len(record):
            # if current position is more than previous position
            if record[i] > record[index]:
                # sequence is not descending
                desc = False
                # if this is the first problem, provide the index. Later we will fix that problem and if there are no others then can be made safe
                if desc_problem_index == None:
                    desc_problem_index = i
            # if current position is less than previous position
            elif record[i] < record[index]:
                #sequence is not ascending
                asc = False
                #if this is the first problem, provide the index. Later we will fix that problem and if there are no others then can be made safe
                if asc_problem_index == None:
                    asc_problem_index = i
            if record[i] == record[index]:
                print("duplicate value")
                return i
            index = i
    # if sequence is ascending or descending and has not broken out with return because of exceeding distance req then it is safe
    if desc or asc:
        print("safe")
        return "safe"
    # if sequence is neither ascending nor descending and has not broken out with return because of exceeding distance req then return problem indices
    else:
        return [desc_problem_index, asc_problem_index]

   
# get input
reports_list = []
with open("input02.txt", "r") as textfile:
    reports = textfile.read().splitlines()
    for report in reports:
        reports_list.append(report.split(" "))
        
# testing materials
# x = [2,4,5,6]
# y = [5,6,4,7,2,1]
# z = [4, 6, 2, 1]


total = 0
records = reports_list
for record in records:
    made_safe = False
    unsafe_indices = []
    

    # run safe. This will return True if safe. Otherwise it will return an index or 2 indices. If an index, test 3 possible sequences. Otherwise test 6
    # if unsafe, fix problem index. run safe. if unsafe discard. if safe total +=1. That gives tolerance of 1 mistake.
    if safe(record) == "safe":
        
        total +=1
    else:
        print("unsafe")
        if isinstance(safe(record), list):
            print("list", safe(record))
            for i in range(len(safe(record))):
                unsafe_indices.append(safe(record)[i])
        else:
            unsafe_indices.append(safe(record))
        
        print("+1 unsafe", safe(record))

    indices_to_test_safety_without = []
    
    if unsafe_indices:

        for unsafe_index in unsafe_indices:
            indices_to_test_safety_without.append(unsafe_index-1)
            indices_to_test_safety_without.append(unsafe_index)
            indices_to_test_safety_without.append(unsafe_index+1)

    # if any of these return True then, once, total +=1
    # print(indices_to_test_safety_without)
    if indices_to_test_safety_without:

        for index_to_test_safety_without in indices_to_test_safety_without:
            #print(record, index_to_test_safety_without, "indextotestsafetywithout")
            old_record = record.copy()
            #print("old record", old_record)
            if 0 <= index_to_test_safety_without <= (len(old_record)-1):
                old_record.pop(index_to_test_safety_without)

            
                if old_record:
                    if safe(old_record) == "safe":
                        made_safe = True
                        break
                else:
                    old_record = record
            
    if made_safe == True:
        total +=1

print(total)

