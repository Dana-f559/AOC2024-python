with open("inputs/01.txt", "r") as file:
    inp = file.read()

line = inp.splitlines()[0]

l_2 = []
id_space = 0

for i in range(0, len(line), 2):
    if int(line[i]) > 0:
        l_2.append([f"{id_space}" for _ in range(int(line[i]))])

    if i < len(line) - 1:
        l_2.append(["." for _ in range( int(line[i + 1]) )])

    id_space += 1

for j in range((len(l_2)-1), 0, -2):
    for i in range(1, j, 2): 
        if len(l_2[j]) > l_2[i].count("."):
            continue

        if l_2[j].count(".") > 0:
            continue
        
        if l_2[i].count(".") == 0:
            continue

        idx = l_2[i].index(".")
        t = [l for l in l_2[i]]

        for l in range(len(l_2[j])):
            t[idx + l] = l_2[j][l]
        
        l_2[i] = t
        l_2[j] = ["." for _ in range(len(l_2[j]))]


l_2 = [l_2[i][j] for i in range(len(l_2)) for j in range(len(l_2[i]))]

count2 = 0
for idx, n in enumerate(l_2):
    if n == ".":
        continue
    count2 += idx * int(n)

print(count2)
