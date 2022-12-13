def get_height(char):
    if char == "S":
        return 0
    if char == "E":
        return 25
    return ord(char) - ord("a")


class Heatmap(list):

    def get(self, pos):
        return self[pos[1]][pos[0]]


with open("data12") as f:
    data = f.read().split("\n")[:-1]

start = (0, 0)
end = (0, 0)
for y in range(len(data)):
    if "S" in data[y]:
        start = (data[y].index("S"), y)
    if "E" in data[y]:
        end = (data[y].index("E"), y)

    data[y] = [get_height(x) for x in data[y]]

hm = Heatmap(data)


# Part 1
paths = [[start]]
final_paths = []
while len(paths) > 0:
    paths_to_delete = paths[:]
    for path in paths:
        pos = path[-1]  # pick last position
        if pos == end:
            final_paths.append(path)
        if pos[1] < len(hm) - 1:  # not at max y
            # add step down
            next_pos = (pos[0], pos[1] + 1)
            if (hm.get(next_pos) <= hm.get(pos) + 1) and \
               next_pos not in [p[-1] for p in paths] and \
               pos != end and \
               next_pos not in path:
                paths.append(path + [next_pos])
        if pos[1] > 0:  # not at min y
            # add step up
            next_pos = (pos[0], pos[1] - 1)
            if (hm.get(next_pos) <= hm.get(pos) + 1) and \
               next_pos not in [p[-1] for p in paths] and \
               pos != end and \
               next_pos not in path:
                paths.append(path + [next_pos])
        if pos[0] > 0:  # not at min x
            # add step left
            next_pos = (pos[0] - 1, pos[1])
            if (hm.get(next_pos) <= hm.get(pos) + 1) and \
               next_pos not in [p[-1] for p in paths] and \
               pos != end and \
               next_pos not in path:
                paths.append(path + [next_pos])
        if pos[0] < len(hm[0]) - 1:  # not at max x
            # add step right
            next_pos = (pos[0] + 1, pos[1])
            if (hm.get(next_pos) <= hm.get(pos) + 1) and \
               next_pos not in [p[-1] for p in paths] and \
               pos != end and \
               next_pos not in path:
                paths.append(path + [next_pos])

    for p in paths_to_delete:
        paths.remove(p)
    paths_to_delete = []

print(min([len(p) for p in final_paths]) - 1)  # -1 to excl. starting position


# Part 2
paths = [[end]]
final_paths = []
while len(paths) > 0:
    paths_to_delete = paths[:]
    for path in paths:
        pos = path[-1]  # pick last position
        if hm.get(pos) == 0:
            final_paths.append(path)
            break  # the first path found is already the shortest
        if pos[1] < len(hm) - 1:  # not at max y
            # add step down
            next_pos = (pos[0], pos[1] + 1)
            if (hm.get(next_pos) >= hm.get(pos) - 1) and \
               next_pos not in [p[-1] for p in paths] and \
               hm.get(pos) != 0 and \
               next_pos not in path:
                paths.append(path + [next_pos])
        if pos[1] > 0:  # not at min y
            # add step up
            next_pos = (pos[0], pos[1] - 1)
            if (hm.get(next_pos) >= hm.get(pos) - 1) and \
               next_pos not in [p[-1] for p in paths] and \
               hm.get(pos) != 0 and \
               next_pos not in path:
                paths.append(path + [next_pos])
        if pos[0] > 0:  # not at min x
            # add step left
            next_pos = (pos[0] - 1, pos[1])
            if (hm.get(next_pos) >= hm.get(pos) - 1) and \
               next_pos not in [p[-1] for p in paths] and \
               hm.get(pos) != 0 and \
               next_pos not in path:
                paths.append(path + [next_pos])
        if pos[0] < len(hm[0]) - 1:  # not at max x
            # add step right
            next_pos = (pos[0] + 1, pos[1])
            if (hm.get(next_pos) >= hm.get(pos) - 1) and \
               next_pos not in [p[-1] for p in paths] and \
               hm.get(pos) != 0 and \
               next_pos not in path:
                paths.append(path + [next_pos])
                # print(paths[-1])

    for p in paths_to_delete:
        paths.remove(p)
    paths_to_delete = []
    if len(final_paths) > 0:
        break

print(min([len(p) for p in final_paths]) - 1)  # -1 to excl. starting position
