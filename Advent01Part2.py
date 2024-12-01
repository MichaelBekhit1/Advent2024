# Given two lists of integers, organise is lists from smallest to largest. Advance through the lists simultaneously
# finding the difference between the two lists for each position and return the total of all the distances

class Solution:
    def find_the_difference(self, first_list:list[int], second_list:list[int]) -> int:
        
        # sort the lists ascending

        first_list = sorted(first_list)
        second_list = sorted(second_list)

        # loop length should be the longest list in case of breaks in the list e.g. [1,2,_,4]

        if len(first_list)>=len(second_list):
            loop_iterations = len(first_list)
        else:
            loop_iterations = len(second_list)

        # initialise var for total difference

        total_difference = 0

        for i in range(loop_iterations):
            # assumes that both lists are the same length
            
            # return absolute value to avoid having to determine which int has greater val
            
            difference = abs(first_list[i] - second_list[i])
            total_difference += difference

        return total_difference
    
    def similarity_score(self, first_list:list[int], second_list:list[int]) -> int:
        
        
        # initialise var total similarity score

        similarity_score= 0

        for value in first_list:
            similarity_score += (value * second_list.count(value))
        
        return similarity_score


        







        

# bring txt input into program
pairs = []
firsts=[]
seconds=[]
with open ('input01.txt','r') as textinput:
    for line in textinput.readlines():
        pairs.append(line.split())
# this for loop can be incorporated into the for loop above        
for pair in pairs:
    firsts.append(int(pair[0]))
    seconds.append(int(pair[1]))


# some test lists
test_first = [1,2,4,6]
test_second = [2,6,4,2]
test_third = [1,2,2]


# a test
x = Solution()
# print(x.find_the_difference(firsts,seconds))
print(x.similarity_score(firsts, seconds))


