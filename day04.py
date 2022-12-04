def get_set(pair):
    """
    convert string "X-Y" to a set containing all numbers [X:Y]
    """
    strrange = pair.split("-")
    return set(range(int(strrange[0]), int(strrange[1])+1))


with open("data04") as f:
    data = f.readlines()

contained = 0
overlapping = 0
for line in data:
    if line.endswith("\n"):
        line = line[:-1]
    pairs = line.split(",")
    elf1 = get_set(pairs[0])
    elf2 = get_set(pairs[1])
    if elf1.issubset(elf2) or elf2.issubset(elf1):
        contained += 1
    if len(elf1 & elf2) > 0:
        overlapping += 1

print(contained)
print(overlapping)
