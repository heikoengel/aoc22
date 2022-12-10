class CRT(object):

    data = [["." for x in range(40)] for y in range(6)]
    row = 0
    col = 0

    def iterate(self, x):
        # draw to CRT
        if self.col in range(x-1, x+2):
            self.data[self.row][self.col] = "#"
        # move to next pixel
        self.col += 1
        if self.col == 40:
            self.col = 0
            self.row += 1
            if self.row == 6:
                self.row = 0


cycle = 0
x = 1
sig_strengths = []
crt = CRT()

with open("data10") as f:
    instr = f.read().split("\n")[:-1]

for op in instr:
    if op == "noop":
        cycle += 1
        sig_strengths.append(x * cycle)
        crt.iterate(x)
    else:  # addx
        val = int(op.split()[1])
        for i in range(2):
            cycle += 1
            sig_strengths.append(x * cycle)
            crt.iterate(x)
        x += val


total_strength_p1 = sum([sig_strengths[x-1] for x in
                         (20, 60, 100, 140, 180, 220)])
print(total_strength_p1)

for row in range(6):
    print("".join(crt.data[row]))
