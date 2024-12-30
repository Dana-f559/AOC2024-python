with open("input.txt") as file:
    lines = file.readlines()


word = "XMAS"
word_backwards = word[::-1]
count = sum([l.count(word) + l.count(word_backwards) for l in lines])


WIDTH = len(lines[0]) -1
HEIGHT = len(lines)

dir_colum = [(0,0), (1,0), (2,0), (3,0)]
for i in range(HEIGHT-3):
    for j in range(WIDTH ):

        positions = [(i + di, j + dj) for di, dj in dir_colum]
       
        colum_word = "".join([lines[x][y] for x, y in positions])
        if colum_word == word or colum_word == word_backwards:
            count += 1

dir_l_dia = [(0,0), (1,1), (2,2), (3,3)]
dir_r_dia = [(0,3), (1,2), (2,1), (3,0)]
for i in range(HEIGHT - 3):
    for j in range(WIDTH - 3):
        positions_l = [(i + di, j + dj) for di, dj in dir_l_dia]
        positions_r = [(i + di, j + dj) for di, dj in dir_r_dia]
        
        l_dia_word = "".join([lines[x][y] for x, y in positions_l])
        r_dia_word = "".join([lines[x][y] for x, y in positions_r])
        
        if l_dia_word == word or l_dia_word == word_backwards:
            count += 1

        if r_dia_word == word or r_dia_word == word_backwards:
            count += 1

print(count)