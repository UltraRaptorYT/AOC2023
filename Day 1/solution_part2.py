with open("input.txt", "r") as f:
    data = f.read().strip()

lines = data.split("\n")

output = []

mapValue = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

for line in lines:
    temp = 0
    numMap = {}
    for numKey, numVal in mapValue.items():
        if numKey in line:
            start_index = 0
            while True:
                idx = line.find(numKey, start_index)
                if idx == -1:
                    break
                numMap[idx] = numVal
                start_index = idx + 1
    for idx, char in enumerate(line):
        if char.isnumeric():
            numMap[idx] = int(char)
    sortedArr = sorted(numMap.items(), key=lambda i: int(i[0]))
    temp = sortedArr[0][1] * 10 + sortedArr[-1][1]
    output.append(temp)

print(sum(output))
