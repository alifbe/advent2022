elves = [0]
with open("input.txt", "r") as fh:
    lines = fh.readlines()

for line in lines:
    line = line.strip()
    if line != "":
        elves[-1] += int(line)
    else:
        elves.append(0)

elves = sorted(elves, reverse=True)
print(elves[0])
print(sum(elves[0:3]))
