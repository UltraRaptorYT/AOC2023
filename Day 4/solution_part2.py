import re

with open("input.txt", "r") as f:
    data = f.read().strip()

games = data.split("\n")

cardInstance = [1] * len(games)

for card in games:
    cardNo, cardsStack = card.split(": ")
    cardNo = int(cardNo.split(" ")[-1])
    winStackStr, currentStackStr = cardsStack.split(" | ")
    winStack = re.findall("\d+", winStackStr)
    currentStack = re.findall("\d+", currentStackStr)
    correctStack = []
    for win in winStack:
        if win in currentStack:
            correctStack.append(int(win))

    for i in range(1, len(correctStack) + 1):
        if cardNo - 1 + i < len(games):
            cardInstance[cardNo - 1 + i] += cardInstance[cardNo - 1]
        else:
            break

print(sum(cardInstance))
