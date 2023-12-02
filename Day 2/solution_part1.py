with open("input.txt", "r") as f:
    data = f.read().strip()

lines = data.split("\n")

output = []

max = {"red": 12, "green": 13, "blue": 14}

for line in lines:
    gameID, game = line.split(": ")
    id = gameID.split(" ")[1]
    valid = True
    for draw in game.split("; "):
        for ball in draw.split(", "):
            ballNum, ballColor = ball.split(" ")
            if int(ballNum) > max[ballColor]:
                valid = False
                continue
            else:
                pass
    if valid:
        output.append(int(id))

print(sum(output))
