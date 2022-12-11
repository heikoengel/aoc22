from copy import deepcopy


def apply_op(op_str, old):
    in1, op, in2 = op_str.split(" ")
    in1 = old if in1 == "old" else int(in1)
    in2 = old if in2 == "old" else int(in2)
    if op == "*":
        return in1 * in2
    else:
        return in1 + in2


def mult_reduce(vals):
    ret = 1
    for f in vals:
        ret *= f
    return ret


with open("data11") as f:
    data = f.read().split("\n")[:-1]

# Parse input data
monkey = 0
state = {}

for line in data:
    if line.startswith("Monkey"):
        monkey = int(line.split()[1][:-1])
        state[monkey] = {'inspected': 0}
    if "Starting items" in line:
        items = [int(x) for x in line.split(":")[1].split(",")]
        state[monkey]['items'] = items
    if "Test:" in line:
        state[monkey]['mod'] = int(line.split("by")[-1])
    if "Operation:" in line:
        state[monkey]['op'] = line.split("=")[-1].strip()
    if "true" in line:
        state[monkey]['true'] = int(line.split()[-1])
    if "false" in line:
        state[monkey]['false'] = int(line.split()[-1])

# take a copy of the initial state for part 2
state_p2 = deepcopy(state)


# Part 1: 20 rounds with worry level reduction by 3
for round in range(20):
    for monkey in range(len(state)):
        for item in state[monkey]['items']:
            wl = apply_op(state[monkey]['op'], item)
            wl = int(wl/3)
            state[monkey]['inspected'] += 1
            if wl % state[monkey]['mod'] == 0:
                dest = state[monkey]['true']
            else:
                dest = state[monkey]['false']
            state[dest]['items'].append(wl)
        state[monkey]['items'] = []

max_inspected = sorted([state[m]['inspected'] for m in state])[-2:]
print(mult_reduce(max_inspected))


# Part 2: 10000 rounds w/o worry level reduction
mod_product = mult_reduce([state_p2[m]['mod'] for m in state_p2])

for round in range(10000):
    for monkey in range(len(state_p2)):
        for item in state_p2[monkey]['items']:
            wl = apply_op(state_p2[monkey]['op'], item)
            state_p2[monkey]['inspected'] += 1
            if wl % state_p2[monkey]['mod'] == 0:
                dest = state_p2[monkey]['true']
            else:
                dest = state_p2[monkey]['false']
            wl = wl % mod_product  # keep worry level manageable
            state_p2[dest]['items'].append(wl)

        state_p2[monkey]['items'] = []

max_inspected = sorted([state_p2[m]['inspected'] for m in state_p2])[-2:]
print(mult_reduce(max_inspected))
