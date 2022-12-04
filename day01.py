with open('data01') as f:
    data = f.readlines()

elves = []
values = []
for line in data:
    if line.endswith("\n"):
        line = line[:-1]
    if line == "":
        elves.append(sum(values))
        values = []
    else:
        val = int(line)
        values.append(val)

elves.append(sum(values))

print(max(elves))
print(sum(sorted(elves)[-3:]))
