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
star_stack_map = {}


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

    validNeighbour = []

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < totalRows and 0 <= new_col < totalCols:
            neighbour.append({"pos": (new_row, new_col), "val": grid[new_row][new_col]})
    for char in neighbour:
        if char["val"] in "*":
            validNeighbour.append(char["pos"])
    return validNeighbour


for rowIdx, row in enumerate(rows):
    numMatch = re.finditer("\d+", row)
    for num in numMatch:
        start_idx = num.start()
        end_idx = num.end()
        numVal = num.group()
        isValid = False
        for i in range(start_idx, end_idx):
            currentCheck = checkNeighbour(i, rowIdx)
            if len(currentCheck) > 0:
                if currentCheck[0] in star_stack_map.keys():
                    star_stack_map[currentCheck[0]].append(int(numVal))
                else:
                    star_stack_map[currentCheck[0]] = [int(numVal)]
                break

import math

for key, val in star_stack_map.items():
    if len(val) > 1:
        output.append(math.prod(val))

print(sum(output))
