

import sys
import re
import numpy as np

pattern = re.compile("(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))")
pattern2 = re.compile("[0-9]+.*[0-9]+")


result = []
nums = []
totalRes = 0
leftorRight = False

for i, line in enumerate(open("input.txt")):
    for match in re.finditer(pattern, line):

        print(match.group())
        result.append(match.group())
        # print("good num")
        
block = True

for index in result:
    if(index == "do()"):
        block = True
    elif(index == "don't()"):
        block = False
    elif(block == True):
        for match in re.finditer(pattern2, index):
            # print(match.group())
            if match:
                nums.append(match.group())
split_list = [string.split() for string in nums]
splitted = []
for v in nums:
    splitted.extend(v.split(','))
print(splitted)

x=0
while(x < len(splitted)):
    # print(splitted[x], "*", splitted[x+1])
    totalRes += (int(splitted[x]) * (int(splitted[x+1])))
    x+=2
    
print(totalRes)


                