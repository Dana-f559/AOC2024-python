with open("inputs/01.txt", "r") as file:
    inp = file.read()

lines = inp.splitlines()

visited = set()

def count_sides(sds):
    sides = 0
    if len(sds) == 0 or sds == {(-1, -1), (-1, 1)}:
        sides += 4

    if sds == {(-1, -1)} or sds == {(-1, 1)}:
        sides += 4

    if sds == {(-1, 0), (-1, 1), (-1, -1)}:
        sides += 4
    
    if sds == {(-1, -1), (-1, 0)} or sds == {(-1, 0), (-1, 1)}:
        sides += 2

    if sds == {(-1, -1), (0, -1)} or sds == {(-1, 1), (0, -1), (-1, -1)}:
        sides += 2

    if sds == {(-1, 0), (0, -1)} or sds == {(-1, 0), (0, -1), (-1, -1)}:
        sides -= 2

    return sides


score = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if (y, x) in visited:
            continue

        cur_symbol = lines[y][x]
        
        dirs = [(-1, 0), (1, 0), (0,-1), (0, 1)]
        sides_dirs = [(-1, -1), (-1, 1),(-1, 0), (0, -1)]


        possible_moves = [(y,x)]
        
        sides = 0

        while True:
            found = False
            for move in possible_moves.copy():
                if move in visited:
                    continue
                
                visited.add(move)
                ts = {
                    (n_y, n_x)
                    for l in dirs
                    if 0 <= (n_y := move[0] + l[0]) < len(lines)
                    and 0 <= (n_x := move[1] + l[1]) < len(lines[0])
                    and lines[n_y][n_x] == cur_symbol
                    and (n_y, n_x) not in possible_moves
                }

                sds = {
                    l
                    for l in sides_dirs
                    if 0 <= (n_y := move[0] + l[0]) < len(lines)
                    and 0 <= (n_x := move[1] + l[1]) < len(lines[0])
                    and lines[n_y][n_x] == cur_symbol
                }

                sides += count_sides(sds)

                if len(ts) != 0:
                    found = True

                possible_moves.extend(ts)  

            if found == False:
                break
        score += sides * len(set(possible_moves))         

print(score)
