import re

with open("input.txt", "r") as f:
    data = f.read().strip()

games = data.split("\n")

output = []

for card in games:
    cardNo, cardsStack = card.split(": ")
    winStackStr, currentStackStr = cardsStack.split(" | ")
    winStack = re.findall("\d+", winStackStr)
    currentStack = re.findall("\d+", currentStackStr)
    # print(winStack, currentStack)
    correctStack = []
    for win in winStack:
        if win in currentStack:
            correctStack.append(int(win))
    currentScore = 0
    for i in correctStack:
        if currentScore == 0:
            currentScore = 1
        else:
            currentScore *= 2
    output.append(currentScore)

print(sum(output))
