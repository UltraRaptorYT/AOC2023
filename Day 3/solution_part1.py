import re

with open("input.txt", "r") as f:
    data = f.read().strip()

rows = data.split("\n")

grid = []
for col in rows:
    grid.append([char for char in col])

totalRows = len(data.split("\n"))
totalCols = len(data.split("\n")[0])

output = []

import string

all_punctuation_without_dot = string.punctuation.replace(".", "")


def checkNeighbour(col, row):
    neighbour = []
    directions = [
        (-1, 0),  # Top
        (1, 0),  # Bottom
        (0, -1),  # Left
        (0, 1),  # Right
        (-1, -1),  # Top-left
        (-1, 1),  # Top-right
        (1, -1),  # Bottom-left
        (1, 1),  # Bottom-right
    ]

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < totalRows and 0 <= new_col < totalCols:
            neighbour.append(grid[new_row][new_col])
    for char in neighbour:
        if char in all_punctuation_without_dot:
            return True
    return False


for rowIdx, row in enumerate(rows):
    numMatch = re.finditer("\d+", row)
    for num in numMatch:
        start_idx = num.start()
        end_idx = num.end()
        numVal = num.group()
        isValid = False
        for i in range(start_idx, end_idx):
            currentCheck = checkNeighbour(i, rowIdx)
            if currentCheck:
                isValid = True
        if isValid:
            output.append(int(numVal))

print(sum(output))
