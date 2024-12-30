with open("input.txt") as file:
    lines = file.readlines()

WIDTH = len(lines[0]) -1
HEIGHT = len(lines)

word = "MAS"
word_backwards = word[::-1]

dirs_l = [(-1,-1),  (0,0), (1,1) ]
dirs_r = [(-1,1), (0,0),(1,-1)]

count = 0

for i in range(1,HEIGHT-1):
    
    for j in range(1,WIDTH-1):
        if lines[i][j] != "A":
            continue
        ps_l = [(i + di, j + dj) for di, dj in dirs_l]
        dir_l_word = "".join([lines[x][y] for x, y in ps_l])

        ps_r = [(i + di, j + dj) for di, dj in dirs_r]
        dir_r_word = "".join([lines[x][y] for x, y in ps_r])
        
        if (dir_l_word == word or dir_l_word == word_backwards) and (dir_r_word == word or dir_r_word == word_backwards):
            count += 1

print(count)