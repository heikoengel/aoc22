def get_score(b):
    if b == "X" or b == "A":
        return 1  # rock
    elif b == "Y" or b == "B":
        return 2  # paper
    else:
        return 3  # scissors


def get_points(a, b):
    if a == b:
        return (3 + a)  # draw
    if a == 1 and b == 2:  # rock paper
        return (6 + 2)
    if a == 1 and b == 3:  # rock scissors
        return (0 + 3)
    if a == 2 and b == 1:  # paper rock
        return (0 + 1)
    if a == 2 and b == 3:  # paper scissors
        return (6 + 3)
    if a == 3 and b == 1:  # scissors rock
        return (6 + 1)
    if a == 3 and b == 2:  # scissors paper
        return (0 + 2)


def get_card(a, result):
    if result == "X":  # lose
        if a == "A":
            return "Z"  # rock -> scissors
        if a == "B":
            return "X"  # paper -> rock
        if a == "C":
            return "Y"  # scissors -> paper
    if result == "Y":  # draw
        if a == "A":
            return "X"  # rock -> rock
        if a == "B":
            return "Y"  # paper -> paper
        if a == "C":
            return "Z"  # scissors -> scissors
    if result == "Z":  # win
        if a == "A":
            return "Y"  # rock -> paper
        if a == "B":
            return "Z"  # paper -> scissors
        if a == "C":
            return "X"  # scissors -> rock


with open("data02") as f:
    data = f.readlines()

results = []
res2 = []
for line in data:
    if line.endswith("\n"):
        line = line[:-1]
    picks = line.split(" ")
    results.append(get_points(get_score(picks[0]), get_score((picks[1]))))

    card = get_card(picks[0], picks[1])
    res2.append(get_points(get_score(picks[0]), get_score((card))))

print(sum(results))
print(sum(res2))
