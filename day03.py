def get_prio(char):
    """
    translate character to priority, lower case 1-26, upper case 27-52
    """
    if char == char.upper():
        return (ord(char) - ord('A') + 27)
    else:
        return (ord(char) - ord('a') + 1)


with open("data03") as f:
    data = f.readlines()

prios_p1 = []
group = []
prios_p2 = []
for line in data:
    if line.endswith("\n"):
        line = line[:-1]

    # part 1
    size = len(line) >> 1
    comp_a = line[:size]  # divide into evenly sized compartments
    comp_b = line[-size:]
    common = list(set(comp_a) & set(comp_b))[0]
    prios_p1.append(get_prio(common))

    # part 2
    group.append(line)
    if len(group) == 3:
        common = list(set(group[0]) & set(group[1]) & set(group[2]))[0]
        prios_p2.append(get_prio(common))
        group = []

print(sum(prios_p1))
print(sum(prios_p2))
