with open("inputs/01.txt", "r") as file:
    inp = file.read()

lines = inp.splitlines()

visited = set()

score = 0

for y in range(len(lines)):
    for x in range(len(lines[0])):
        if (y, x) in visited:
            continue

        cur_symbol = lines[y][x]
        
        dirs = [(-1, 0), (1, 0), (0,-1), (0, 1)]

        possible_moves = [(y,x)]
        
        walls = 0

        while True:
            found = False
            for move in possible_moves.copy():

                if move in visited:
                    continue

                visited.add(move)
                ns = {
                    (n_y, n_x)
                    for l in dirs
                    if 0 <= (n_y := move[0] + l[0]) < len(lines)
                    and 0 <= (n_x := move[1] + l[1]) < len(lines[0])
                    and lines[n_y][n_x] == cur_symbol
                }
                ts = {n for n in ns if (n[0], n[1]) not in possible_moves}

                if len(ts) != 0:
                    found = True

                possible_moves.extend(ts)  

                walls += 4 - len(ns)
            
            if found == False:
                break
        
        
        score += walls * len(set(possible_moves)) 


print(score)
