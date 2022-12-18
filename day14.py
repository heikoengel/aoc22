class Grid(object):

    def __init__(self, min_x, min_y, max_x, max_y):
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y
        self.data = [["." for x in range(max_x - min_x + 1)]
                     for y in range(max_y - min_y + 1)]

    def __getitem__(self, vec):
        return self.data[vec[1] - self.min_y][vec[0] - self.min_x]

    def __setitem__(self, vec, val):
        self.data[vec[1] - self.min_y][vec[0] - self.min_x] = val

    def __repr__(self):
        i = 0
        ret = ""
        for line in self.data:
            ret += "%3d %s\n" % (i, "".join(line))
            i += 1
        return ret


with open("data14") as f:
    data = f.read().split("\n")[:-1]

min_x = 500
max_x = 500
min_y = 0
max_y = 0


paths = []
for line in data:
    vectors = line.split(" -> ")
    path = []
    for vector in vectors:
        x, y = [int(v) for v in vector.split(",")]
        min_x = min(x, min_x)
        max_x = max(x, max_x)
        min_y = min(y, min_y)
        max_y = max(y, max_y)
        path.append((x, y))
    paths.append(path)

floor = max_y + 2
grid = Grid(min_x - floor, min_y, max_x + floor, floor)

for path in paths:
    for i in range(len(path) - 1):
        x_min = min(path[i][0], path[i+1][0])
        x_max = max(path[i][0], path[i+1][0])
        for x in range(x_min, x_max + 1):
            y = path[i][1]
            grid[(x, y)] = "#"
        y_min = min(path[i][1], path[i+1][1])
        y_max = max(path[i][1], path[i+1][1])
        for y in range(y_min, y_max + 1):
            x = path[i][0]
            grid[(x, y)] = "#"

# add floor for part 2
for x in range(grid.min_x, grid.max_x + 1):
    grid[(x, floor)] = "#"

print(grid)

units = 0
p1_units = 0
off = False
while not off:
    pos = (500, 0)
    while True:
        # part 1: sand unit below lowest wall
        if pos[1] == floor - 1 and p1_units == 0:
            p1_units = units

        npos = (pos[0], pos[1] + 1)  # one down
        if grid[npos] == ".":
            pos = npos
            continue

        npos = (pos[0] - 1, pos[1] + 1)  # one down, one left
        if grid[npos] == ".":
            pos = npos
            continue

        npos = (pos[0] + 1, pos[1] + 1)  # one down, one right
        if grid[npos] == ".":
            pos = npos
            continue

        # can't move anywhere, come to rest
        grid[pos] = "o"
        units += 1

        # Part 2: sand units reached entry point
        if pos == (500, 0):
            off = True
            break
        break

# print(grid)
print(p1_units)
print(units)
