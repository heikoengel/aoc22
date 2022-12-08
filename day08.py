with open("data08") as f:
    data = f.read().split("\n")[:-1]

for i in range(len(data)):
    data[i] = [int(x) for x in data[i]]

num_visible = 0
scenic_scores = []

width = len(data[0])
height = len(data)

for x in range(width):
    for y in range(height):

        # check visibility to the left
        visible_left = True
        score_left = 0
        for i in range(x-1, -1, -1):
            score_left += 1
            if data[y][i] < data[y][x]:
                visible_left = True
            else:
                visible_left = False
                break

        # check visibility to the top
        score_top = 0
        visible_top = True
        for i in range(y-1, -1, -1):
            score_top += 1
            if data[i][x] < data[y][x]:
                visible_top = True
            else:
                visible_top = False
                break

        # check visibility to the right
        visible_right = True
        score_right = 0
        for i in range(x+1, width):
            score_right += 1
            if data[y][i] < data[y][x]:
                visible_right = True
            else:
                visible_right = False
                break

        # check visibility to the bottom
        visible_bottom = True
        score_bottom = 0
        for i in range(y+1, height):
            score_bottom += 1
            if data[i][x] < data[y][x]:
                visible_bottom = True
            else:
                visible_bottom = False
                break

        if visible_left or visible_top or visible_right or visible_bottom:
            num_visible += 1

        scenic_scores.append(score_left * score_top *
                             score_right * score_bottom)


print(num_visible)
print(max(scenic_scores))
