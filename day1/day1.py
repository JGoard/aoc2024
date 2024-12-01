# Day 1 AOC 2024: Finding the difference/distance between each number in a line
# In the example list above, the pairs and distances would be as follows:

###
# Pt. 1
###
# The smallest number in the left list is 1, and the smallest number in the right list is 3. The distance between them is 2.
# The second-smallest number in the left list is 2, and the second-smallest number in the right list is another 3. The distance between them is 1.
# The third-smallest number in both lists is 3, so the distance between them is 0.
# The next numbers to pair up are 3 and 4, a distance of 1.
# The fifth-smallest numbers in each list are 3 and 5, a distance of 2.
# Finally, the largest number in the left list is 4, while the largest number in the right list is 9; these are a distance 5 apart.
# To find the total distance between the left list and the right list, add up the distances between all of the pairs you found. In the example above, this is 2 + 1 + 0 + 1 + 2 + 5, a total distance of 11!import re

###
# Pt. 2
###
# For these example lists, here is the process of finding the similarity score:

# The first number in the left list is 3. It appears in the right list three times, so the similarity score increases by 3 * 3 = 9.
# The second number in the left list is 4. It appears in the right list once, so the similarity score increases by 4 * 1 = 4.
# The third number in the left list is 2. It does not appear in the right list, so the similarity score does not increase (2 * 0 = 0).
# The fourth number, 1, also does not appear in the right list.
# The fifth number, 3, appears in the right list three times; the similarity score increases by 9.
# The last number, 3, appears in the right list three times; the similarity score again increases by 9.
# So, for these example lists, the similarity score at the end of this process is 31 (9 + 4 + 0 + 0 + 9 + 9).

import numpy as np 
from numpy import sort

totalDistance = 0   # Total distance between the left list and the right list
totalSimilarity = 0 # Total similarity score between left list and right list
tempSimilarity = 0  # Temporary holding value for similarity score calculation
sortedArray = []    # Holds sorted 2D array of left and right list

###
# Read input file and strip, split and store into 2D array
###
f = open("input.txt", "r")  # Open input file
lines = f.readlines()       # Read input file and readlines into 2D array
array = [line.strip().split() for line in lines]    # Split lines into 2D array, and strip whitespace from each line
# Basic sorting procedure for lowest to highest number. 
# I was having issue determining how to effectively each column of a 2D array.
sortedArray = np.sort(array, axis = 0)
# print(sortedArray)

###
# Sort each array lowest to highest and calculate totalDistance and totalSimilarity score
###
# Now, manually calculate the distance between each number in the left list and the right list
# The similarity score is also calculated in this loop
for x in sortedArray:
    totalDistance = totalDistance + abs(int(x[1]) - int(x[0]))  # Sum total distance
    for y in sortedArray:       # Loop again through sorted array to calculate similarity
        if x[0] == y[1]:        # Match found, increment similarity
            tempSimilarity = tempSimilarity + 1
        totalSimilarity = totalSimilarity + tempSimilarity * int(x[0])
        tempSimilarity = 0      # Reset to 0
###
# Here are the Answers
###
print("Pt 1. Total Distance is...", totalDistance)
print("Pt 2. Total Similarity is...", totalSimilarity)            
