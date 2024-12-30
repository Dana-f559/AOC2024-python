with open("input.txt", "r") as file:
        inp = file.read()


lines = inp.splitlines()

pos = []

for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] != ".":
            pos.append((lines[y][x],x, y))

count1 = 0

loc_anti1 = set()

def calc_next_position(node1:tuple[str, int, int],node2:tuple[str, int, int]):
    x = node1[1] - node2[1]
    y = node1[2] - node2[2]

    up_x, up_y = node1[1] + x, node1[2] + y
    down_x, down_y = node2[1] - x, node2[2] - y
    
    return up_x, up_y, down_x, down_y

for i in range(len(pos)):
    for j in pos[i+1:]:
        if pos[i][0] != j[0]:
             continue

        up_x, up_y, down_x, down_y = calc_next_position(pos[i], j)


        if (0 <= up_x < len(lines[0])) and (0 <= up_y < len(lines)):
            if (up_x, up_y) not in loc_anti1:
                count1 += 1
                loc_anti1.add((up_x, up_y))
            

        if (0 <= down_x < len(lines[0])) and (0 <= down_y < len(lines)) :
            if (down_x, down_y) not in loc_anti1:
                count1 += 1
                loc_anti1.add((down_x, down_y))

print(count1)