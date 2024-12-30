with open("inputs/01.txt", "r") as file:
        inp = file.read()


lines = inp.splitlines()

score = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        
        if lines[y][x] != "0":
            continue      
        
        dirs = [(-1, 0), (1, 0), (0,-1), (0, 1)]
        
        # PART ONE
        posible_moves = {(y,x)}

        # PART TWO
        # posible_moves = [(y,x)]
        for i in range(0, 9):
            for move in posible_moves.copy():       
                ts = {
                    (n_y, n_x)
                    for l in dirs
                    if 0 <= (n_y := move[0] + l[0]) < len(lines)
                    and 0 <= (n_x := move[1] + l[1]) < len(lines[0])
                    and int(lines[n_y][n_x]) == i + 1
                }

                posible_moves.update(ts)
                # PART TWO 
                # posible_moves.extend(ts)
                posible_moves.remove(move)

        score += len(posible_moves)


print(score)