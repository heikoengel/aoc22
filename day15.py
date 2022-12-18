from re import match
import sys


def get_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


class PosRange(object):

    data = []

    def add(self, frm, to):
        self.data = {*self.data, *range(frm, to + 1)}

    def excl(self, frm, to):
        self.data -= {*range(frm, to + 1)}


with open("data15") as f:
    data = f.read().split("\n")[:-1]

locs = []
for line in data:
    grp = match(rf".*x=(-*\d+), y=(-*\d+): .*x=(-*\d+), y=(-*\d+)", line)
    sx = int(grp[1])
    sy = int(grp[2])
    bx = int(grp[3])
    by = int(grp[4])
    d = get_distance((sx, sy), (bx, by))
    locs.append({'s': (sx, sy), 'b': (bx, by), 'd': d})


# Part 1
nbr = PosRange()

for loc in locs:
    sx = loc['s'][0]
    sy = loc['s'][1]
    sb_dist = loc['d']  # max sensor->beacon distance, y direction
    rs_dist = abs(sy - 2000000)  # row->sensor distance, y direction
    if rs_dist <= sb_dist:
        diff = sb_dist - rs_dist
        nbr.add(sx - diff, sx + diff)

    if loc['b'][1] == 2000000:  # exclude beacons
        nbr.excl(loc['b'][0], loc['b'][0])

print(len(list(nbr.data)))


# Part 2
for y in range(0, 4000001):
    x = 0
    sys.stdout.write("%s\r" % (y))
    for loc in sorted(locs, key=lambda k: k['s'][0]):
        # iterate over all sensors, left to right
        sx = loc['s'][0]
        sy = loc['s'][1]
        sb_dist = loc['d']  # total sensor->beacon distance
        rs_dist = abs(sy - y)  # row->sensor distance in y direction
        x_dist = sb_dist - rs_dist  # remaining distance in x
        if x in range(sx - x_dist, sx + x_dist + 1):
            x = sx + x_dist + 1  # move x to rightmost pos after current sensor

    if x < 4000000:
        freq = x * 4000000 + y
        print(freq)
        exit()
