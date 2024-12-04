# AOC 2024 Day 4: Hopefully this isn't as painful as it looks

import numpy as np
import re
import sys
array = []
Part1Total = 0
Part2Total = 0
# Read input file and strip, split and store into 2D array
f = open("input.txt", "r", encoding='latin-1')  # Open input file
lines = f.readlines()       # Read input file and readlines into 2D array

def VerticalXMAS(input):
    result = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if i <= len(input) - 4:
                down = input[i][j] + input[i+1][j] + input[i+2][j] + input[i+3][j]
                if down == 'XMAS':
                    result += 1
            if i >= 3:
                up = input[i][j] + input[i-1][j] + input[i-2][j] + input[i-3][j]
                if up == 'XMAS':
                    result += 1
    return result

def HorizontalXMAS(input):
    result = 0
    for i in range(len(input)):
        for j in range(len(input[i])-3):
            if input[i][j:j+4] == 'XMAS' or input[i][j:j+4] == 'SAMX':
                result += 1
    return result

def DiagonalXMAS(input):
    result = 0
    for i in range(len(input)):         # For every row
        for j in range(len(input[i])):  # For every column
            if i <= len(input) -4 and j <= len(input[i]) - 4:
                if j + 3 < len(input[i+1]) and j + 3 < len(input[i+2]) and j + 3 < len(input[i+3]):
                    right = input[i][j] + input[i+1][j+1] + input[i+2][j+2] + input[i+3][j+3]
                    if right == "XMAS":
                        result += 1

            if i <= len(input) -4 and j >= 3:
                if j-3 > 0 and j-2 > 0 and j-1 > 0:
                    left = input[i][j] + input[i+1][j-1] + input[i+2][j-2] + input[i+3][j-3]
                    if left == "XMAS":
                        result += 1

            if i <= len(input) +4 and j >= -4:
                if j-3 > 0 and j-2 > 0 and j-1 > 0:
                    left = input[i][j] + input[i+1][j-1] + input[i+2][j-2] + input[i+3][j-3]
                    if left == "XMAS":
                        result += 1
    return result

print (VerticalXMAS(lines) + HorizontalXMAS(lines) + DiagonalXMAS(lines))
