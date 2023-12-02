with open("input.txt", "r") as f:
    data = f.read().strip()

lines = data.split("\n")

output = []

for line in lines:
    temp = 0
    for char in line:
        if char.isnumeric():
            temp += int(char) * 10
            break
    for char in line[::-1]:
        if char.isnumeric():
            temp += int(char)
            break
    output.append(temp)

print(sum(output))
