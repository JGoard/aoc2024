# Day 3 AOC 2024: Multiply them numbers that are listed by mul, or have do/dont statements next to them 
# Part 1:
# The computer appears to be trying to run a program, but its memory (your puzzle input) is 
# corrupted. All of the instructions have been jumbled up!

# It seems like the goal of the program is just to multiply some numbers. 
# It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers. 
# For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024. Similarly, mul(123,4) would multiply 123 by 4.

# However, because the program's memory has been corrupted, there are also many invalid characters that should be ignored, 
# even if they look like part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.
#
# Part 2: 
# There are two new instructions you'll need to handle:
# The do() instruction enables future mul instructions.
# The don't() instruction disables future mul instructions.
# Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are enabled.
# For example:
# xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))

import sys          # For sys.exit
import re           # Regex
import numpy as np  # For sorting
##
# Since I'd rather not write a parser since I have a life, I'm opting for plain "simple" Regex
##
pattern = re.compile("(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))")   # Wow, look at that longness
pattern2 = re.compile("[0-9]+.*[0-9]+")                             


result = []     # Array to store results
nums = []       # Array to store numbers
totalRes = 0    # Total result

##
# Read input file and strip, split and store into 2D array
# Regex find matches for do, dont, and muls
##
for i, line in enumerate(open("input.txt")):
    for match in re.finditer(pattern, line):
        result.append(match.group())
        
block = True # True = do, False = don't for blocking the multiplication function

##
# Regex find matches for mul, and choosing between the do's and don'ts for multiplication
##
for index in result:
    if(index == "do()"):    # If it's a do
        block = True
    elif(index == "don't()"):# If it's a don't
        block = False
    elif(block == True):    # If it's a do
        for match in re.finditer(pattern2, index): # Regex for mul
            if match:
                nums.append(match.group())
##
# Split the 2D array into 2D array of numbers and strings
##
splitted = []
split_list = [string.split() for string in nums] # split each left and right side of the mul instruction
# for splitting each mul string into 2 numbers
for v in nums:
    splitted.extend(v.split(','))
print(splitted)

##
# I took the lazy way out and just added the numbers together and since it had to be an even number of numbers,
# I always know that the next number/index will be the multiplier, hence the x+=2
##
x=0
while(x < len(splitted)):
    totalRes += (int(splitted[x]) * (int(splitted[x+1])))
    x+=2
    
# Bob's your uncle. Prints out only the part 2 answer due to the rework
print(totalRes)


                