with open("data06") as f:
    data = f.readline()
    if data.endswith("\n"):
        data = data[:-1]


def get_marker_pos(num_chars):
    for i in range(0, len(data)-num_chars):
        if len(set(data[i:i+num_chars])) == num_chars:
            return (i+num_chars)


print(get_marker_pos(4))
print(get_marker_pos(14))
