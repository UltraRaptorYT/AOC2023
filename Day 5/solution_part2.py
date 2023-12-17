with open("input.txt", "r") as f:
    data = f.read().strip()

maps = data.split("\n\n")
seeds = maps[0]
mappings = maps[1:]

seeds = seeds.split(": ")[-1].split(" ")

seeds = list(map(int, seeds))

mappedRanges = []

seedRanges = []
for i in range(0, len(seeds), 2):
    seedRanges.append((seeds[i], seeds[i] + seeds[i + 1]))

for mapRange in mappings:
    lines = mapRange.split("\n")
    lines = lines[1:]
    currentRange = []
    for rangeList in lines:
        currentRange.append(tuple(map(int, rangeList.split())))
    currentRange.sort(key=lambda x: x[1])
    mappedRanges.append(currentRange)


def remap(lo, hi, m):
    # Remap an interval (lo,hi) to a set of intervals m
    ans = []
    for dst, src, R in m:
        end = src + R - 1
        D = dst - src  # How much is this range shifted

        if not (end < lo or src > hi):
            ans.append((max(src, lo), min(end, hi), D))

    for i, interval in enumerate(ans):
        l, r, D = interval
        yield (l + D, r + D)

        if i < len(ans) - 1 and ans[i + 1][0] > r + 1:
            yield (r + 1, ans[i + 1][0] - 1)

    # End and start ranges can use some love
    if len(ans) == 0:
        yield (lo, hi)
        return

    if ans[0][0] != lo:
        yield (lo, ans[0][0] - 1)
    if ans[-1][1] != hi:
        yield (ans[-1][1] + 1, hi)


answer = None

for seedStart, seedEnd in seedRanges:
    currentRange = [(seedStart, seedEnd - 1)]
    newRange = []
    for m in mappedRanges:
        for start, end in currentRange:
            for new_interval in remap(start, end, m):
                newRange.append(new_interval)
        currentRange, newRange = newRange, []

    for start, _ in currentRange:
        if answer == None:
            answer = start
        else:
            answer = min(answer, start)

print(answer)
