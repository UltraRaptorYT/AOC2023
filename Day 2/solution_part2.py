with open("input.txt", "r") as f:
    data = f.read().strip()

lines = data.split("\n")

output = []

for line in lines:
    game = line.split(": ")[1]
    gameMap = {}
    for draw in game.split("; "):
        for ball in draw.split(", "):
            ballNum, ballColor = ball.split(" ")
            if ballColor not in gameMap:
                gameMap[ballColor] = int(ballNum)
            else:
                if gameMap[ballColor] < int(ballNum):
                    gameMap[ballColor] = int(ballNum)
    power = 1
    for num in gameMap.values():
        power *= num
    output.append(power)
print(sum(output))
