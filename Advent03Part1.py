# amongst the input data are expressions of the form "mul(?,?)" where ? are integers. Extract these and evaluate them as
# multiplications and total the result

import re

dummy_string = "fsjhkdsjkdjskdsmul(4,6)"

# print(re.search(("(mul)\S\d\S\d\S"),dummy_string))

# print(re.findall(("(mul\(\d\,\d\))"),dummy_string))

results = []
data = []


with open("input03.txt", "r") as textfile:
    for line in textfile.readlines():
        # results.append(re.findall("(mul\(\d\,\d\))"), line)
        data.append(line)

data = "".join(data)
# print(isinstance(data, str))
results = re.findall("(mul\([\\d]+,[\\d]+\))", data)
total = 0
for result in results:
    result = result.replace(",", "*")
    result = result.replace("mul", "")
    total+=eval(result)

print(total)