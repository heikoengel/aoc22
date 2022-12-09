class Rope(object):

    knots = [{'x': 0, 'y': 0} for x in range(10)]

    def move_head(self, dir):
        if dir == "U":
            self.knots[0]['y'] += 1
        elif dir == "D":
            self.knots[0]['y'] -= 1
        elif dir == "R":
            self.knots[0]['x'] += 1
        elif dir == "L":
            self.knots[0]['x'] -= 1

    def move_knot(self, i):
        # get distance vector to previous knot
        dist_vec = {'x': self.knots[i-1]['x'] - self.knots[i]['x'],
                    'y': self.knots[i-1]['y'] - self.knots[i]['y']}
        # move knot based on the distance vector
        if abs(dist_vec['x']) > 1 and abs(dist_vec['y']) <= 1:
            self.knots[i]['x'] += int(dist_vec['x'] / 2)
            self.knots[i]['y'] = self.knots[i-1]['y']
        elif abs(dist_vec['y']) > 1 and abs(dist_vec['x']) <= 1:
            self.knots[i]['x'] = self.knots[i-1]['x']
            self.knots[i]['y'] += int(dist_vec['y'] / 2)
        else:  # abs(distance) == 2 in both directions
            self.knots[i]['x'] += int(dist_vec['x'] / 2)
            self.knots[i]['y'] += int(dist_vec['y'] / 2)


with open("data09") as f:
    data = f.read().split("\n")[:-1]

r = Rope()
positions_p1 = set()
positions_p2 = set()

for instr in data:
    dir, steps = instr.split()
    for step in range(int(steps)):
        r.move_head(dir)
        for knot in range(1, len(r.knots)):
            r.move_knot(knot)
        positions_p1 |= set([(r.knots[1]['x'], r.knots[1]['y'])])
        positions_p2 |= set([(r.knots[9]['x'], r.knots[9]['y'])])

print(len(positions_p1))
print(len(positions_p2))
