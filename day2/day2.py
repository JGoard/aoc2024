# Day 2 AOC 2024: Find which reports on each are safe
# In the example list above, the pairs and distances would be as follows:
# So, a report only counts as safe if both of the following are true:

# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.
# In the example above, the reports can be found safe or unsafe by checking those rules:

# 7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
# 1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
# 9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
# 1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
# 8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
# 1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.

import numpy as np
isIncreasing = False
isDecreasing = False 
safeTotal = 0
unsafeTotal = 0
prevLevel = 0
###
# Read input file and strip, split and store into 2D array
###
f = open("input.txt", "r")  # Open input file
lines = f.readlines()       # Read input file and readlines into 2D array
array = [line.strip().split() for line in lines]    # Split lines into 2D array, and strip whitespace from each line
for report in array:
    report_length = len(report)
    print(report, report_length)
    for level in report:
        if  prevLevel == 0:
            prevLevel = int(level) # Store previous level
        elif ((int(level) - prevLevel) > 3):
            unsafeTotal += 1
            print("Unsafe: Rapid Increase")
            isIncreasing = False
            isDecreasing = False
            break
        elif ((int(level) - prevLevel) < -3):
            unsafeTotal += 1
            isIncreasing = False
            isDecreasing = False
            print("Unsafe: Rapid Decrease")
            break
        elif ((int(level) - prevLevel) == 0):
            unsafeTotal += 1
            isIncreasing = False
            isDecreasing = False
            print("Unsafe: Equal")
            break
        else: # Level is increasing or decreasing by 1, 2, or 3
           if int(level) - prevLevel <= 3 and (int(level) - prevLevel > 0):
               isIncreasing = True
           elif int(level) - prevLevel >= -3 and (int(level) - prevLevel < 0):
               isDecreasing = True
           if isIncreasing and isDecreasing:
               unsafeTotal += 1
               break
        # print(level)
        prevLevel = int(level)  
    isIncreasing = False
    isDecreasing = False
    prevLevel = 0
print("Unsafe Total is...", unsafeTotal)
print("Safe Total is...", len(array) - unsafeTotal)