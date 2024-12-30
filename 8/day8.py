with open("inputs/01.txt", "r") as file:
        inp = file.read()


lines = inp.splitlines()

pos = []

for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] != ".":
            pos.append((lines[y][x],x, y))



def calc_next_position(node1:tuple[str, int, int],node2:tuple[str, int, int]):
    x = node1[1] - node2[1]
    y = node1[2] - node2[2]

    up_x, up_y = node1[1] + x, node1[2] + y
    down_x, down_y = node2[1] - x, node2[2] - y
    
    return up_x, up_y, down_x, down_y

loc_anti2 = set()
count2 = 0


for i in range(len(pos)):
    for j in pos[i+1:]:

        if pos[i][0] != j[0]:
             continue
        
        node1 = pos[i]
        node2 = j

        step_x = node1[1] - node2[1]
        step_y = node1[2] - node2[2]

        safe_up = True
        safe_down = True

        while  safe_up == True or safe_down == True:
            
            if not (0 <= node1[1] < len(lines[0])) or not (0 <= node1[2] < len(lines)):
                safe_up = False
            
            if not (0 <= node2[1] < len(lines[0])) or not (0 <= node2[2] < len(lines)):
                safe_down = False


            up_x, up_y = node1[1] + step_x, node1[2] + step_y
            down_x, down_y = node2[1] - step_x, node2[2] - step_y


            if safe_up and (0 <= up_x < len(lines[0])) and (0 <= up_y < len(lines)):
                if (up_x, up_y) not in loc_anti2  and lines[up_y][up_x] == ".":
                    count2 += 1
                    loc_anti2.add((up_x, up_y))

            if safe_down and (0 <= down_x < len(lines[0])) and (0 <= down_y < len(lines)) :
                if (down_x, down_y) not in loc_anti2 and lines[down_y][down_x] == ".":
                    count2 += 1
                    loc_anti2.add((down_x, down_y))

            node1 = (node1[0], up_x, up_y)
            
            node2 = (node1[0], down_x, down_y)

count2 += len(pos)

print(count2)
