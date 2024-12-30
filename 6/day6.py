with open("input.txt", "r") as file:
        inp = file.read()

lines = inp.splitlines()

cur_str = "^"
cur = (0, 0)


for idx, l in enumerate(lines):
    if cur_str in l:
        cur = (l.index(cur_str), idx)

cur_org = cur

dirr = (0,-1)

loops_count = 0


visited = set()

while True:
    visited.add(cur)
    nx = cur[0] + dirr[0]
    ny = cur[1] + dirr[1]
    
    if nx < 0 or ny < 0: 
        break
    
    if nx >= len(lines[0]) or ny >= len(lines):
         break
    
    if lines[ny][nx] != "#":
        cur = (nx, ny)
        
    else:
        dirr = (-dirr[1], dirr[0])

loops_count = 0

timeout = len(lines) * len(lines[0])
for v in visited:
    cur = cur_org
    dirr = (0,-1)
    
    x = 0
    while True:
        if x >= timeout:
            loops_count += 1
            break
        x += 1

        nx = cur[0] + dirr[0]
        ny = cur[1] + dirr[1]


        if nx < 0 or ny < 0: 
            break
        
        if nx >= len(lines[0]) or ny >= len(lines):
            break
        
        if lines[ny][nx] != "#" and (nx, ny) != v:
            cur = (nx, ny)
            
        else:
            dirr = (-dirr[1], dirr[0])
