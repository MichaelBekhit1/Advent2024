# remove all data between the expression "don't()" and "do()". Repeat Part1

import re

# dummy_string = """mul(374,785)@ /don't()how(!)%select() -how()#who()*^mul(113,822)from()%what()/from()mul(305,505)what())<&~from()mul(841,37)when()#(select()& /mul(879,852)]from()/mul(485,947)?where(276,795)<how(538,951)when()mul(17,660); mul(209,54)<+;from()mul(108,833)~where()*{<mul(312,605)(?#*what()(do()mul(776,879)'how(307,641))!,do()-where()^"""

# dont = re.findall("(don't\(\))", dummy_string)
# do = re.findall("(do\(\))", dummy_string)
# dummy_string = dummy_string.replace("!",".")
# dont_to_do = re.findall("don't\(\).*?do\(\)", dummy_string)
# dont_to_do = "".join(dont_to_do)
# dummy_string = dummy_string.replace(dont_to_do, "")
# print(dummy_string)

results = []
data = []


with open("input03.txt", "r") as textfile:
    for line in textfile.readlines():
        # results.append(re.findall("(mul\(\d\,\d\))"), line)
        data.append(line)
data.insert(0,"do()")
data = "".join(data)

# dont_to_do = re.findall("don't\(\).*?do\(\)", data, re.DOTALL)

# dont_to_do = "".join(dont_to_do)
# for i in dont_to_do:
  #   i = "".join(i)
  #   data = data.replace(i, "#")

# data = data.replace(dont_to_do, "#")
# print(dont_to_do)
# print(data)

# trying a different approach
# create a range from start to finish where start is dont and finish is do

# make into a while loop to repeat - should do the trick ###########################################################

modified = True
valid_data = []

# I realised that my while loop is excluding the default=true data before the first do. wrong answer 87999962
# wrong because there is a dont before the first do. 





while modified == True:
    modified = False
    do_position = re.search(r"do\(\)", data)
    dont_position = re.search(r"don't\(\)", data)
    if do_position:
        modified = True
        start = do_position.end()
        if dont_position:
            
            end = dont_position.start()
            
            valid_data.append(data[start:end])
            data = data[end + len("don't()"):]
        else:
            valid_data.append(data[start:])
            modified = False
    
        
    

# print(valid_data)

# print(dont_position)

valid_data = "".join(valid_data)

results = re.findall("(mul\([\\d]+,[\\d]+\))", valid_data)
total = 0
for result in results:
    result = result.replace(",", "*")
    result = result.replace("mul", "")
    total+=eval(result)
    
# wrong answer 85193019
print(total)


