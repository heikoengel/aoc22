from json import loads
from functools import cmp_to_key


def compare_int(in1, in2):
    if in1 == in2:
        return 0
    elif (in1 < in2):
        return -1
    else:
        return 1


def compare_list(in1, in2):
    in1 = [in1] if isinstance(in1, int) else in1
    in2 = [in2] if isinstance(in2, int) else in2
    min_len = min([len(in1), len(in2)])
    for i in range(min_len):
        if isinstance(in1[i], int) and isinstance(in2[i], int):
            ret = compare_int(in1[i], in2[i])
        else:
            ret = compare_list(in1[i], in2[i])
        if ret:
            return ret

    if len(in1) == len(in2):
        # equal in length, but identical
        return 0
    # left runs out first -> True, else False
    if (len(in1) < len(in2)):
        return -1
    else:
        return 1


with open("data13") as f:
    data = f.read().split("\n")[:-1]

i = 0
pairs = []
packets = []
while i < len(data):
    input1 = loads(data[i])
    input2 = loads(data[i+1])
    i += 3  # skip empty line
    pairs.append([input1, input2])
    packets.append(input1)
    packets.append(input2)


# Part 1
in_order_indices = [i+1 for i in range(len(pairs)) if
                    compare_list(pairs[i][0], pairs[i][1]) == -1]
print(sum(in_order_indices))


# Part 2

# add divider packets
packets.append([[2]])
packets.append([[6]])

key = cmp_to_key(compare_list)
sorted_packets = sorted(packets, key=key)
print((sorted_packets.index([[2]])+1) * (sorted_packets.index([[6]])+1))
