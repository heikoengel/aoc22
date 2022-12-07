stacks_p1 = {}
stacks_p2 = {}
for stack in range(1, 10):
    stacks_p1[stack] = []
    stacks_p2[stack] = []

with open("data05") as f:
    for i in range(1, 9):  # read lines 1-8
        line = f.readline()
        for stack in range(1, 10):  # pos 1-9
            pos = 1 + (4*(stack-1))
            if len(line) < pos:
                continue
            elif line[pos] != " ":
                stacks_p1[stack].append(line[pos])
                stacks_p2[stack].append(line[pos])

    for line in f.readlines():
        if line.endswith("\n"):
            line = line[:-1]
        if "move" not in line:
            continue  # skip remaining header lines
        _, items, _, src, _, dst = line.split()
        items = int(items)
        src = int(src)
        dst = int(dst)

        # Part 1: move one at a time, inverting the order at the destination
        to_be_moved_p1 = stacks_p1[src][:items]  # copy crates to be moved
        stacks_p1[src] = stacks_p1[src][items:]  # remove from source stack
        for crate in to_be_moved_p1:
            stacks_p1[dst].insert(0, crate)  # add to destination stack

        # Part 2: move all crates at once, retaining the original order
        to_be_moved_p2 = stacks_p2[src][:items]  # copy crates to be moved
        stacks_p2[src] = stacks_p2[src][items:]  # remove from source stack
        for crate in reversed(to_be_moved_p2):
            stacks_p2[dst].insert(0, crate)  # add to destination stack


print("".join("%s" % stacks_p1[x][0] for x in sorted(stacks_p1)))
print("".join("%s" % stacks_p2[x][0] for x in sorted(stacks_p2)))
