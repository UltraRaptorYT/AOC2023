with open("input.txt", "r") as f:
    data = f.read().strip()

maps = data.split("\n\n")
seeds = maps[0]
mappings = maps[1:]

seeds = seeds.split(": ")[-1].split(" ")

seeds = list(map(int, seeds))

mappedRanges = []

for mapRange in mappings:
    lines = mapRange.split("\n")
    lines = lines[1:]
    currentRange = []
    for rangeList in lines:
        currentRange.append(list(map(int, rangeList.split())))
    mappedRanges.append(currentRange)

location = []

for seed in seeds:
    currentMap = seed
    for m in mappedRanges:
        for dst, src, rangeLen in m:
            if src <= currentMap and currentMap < src + rangeLen:
                currentMap = dst + (currentMap - src)
                break
    location.append(currentMap)

print(min(location))
