with open("inputs/01.txt", "r") as file:
        inp = file.read()

line = inp.splitlines()[0]

l_1 = []

id_space = 0

for i in range(0,len(line),2):
    for x in range(int(line[i])):
        l_1.append(f"{id_space}" ) 

    if i < len(line)-1:
        for x in range(int(line[i+1])):   
            l_1.append(".")
    
    id_space += 1


i = 0
j = len(l_1) - 1

while i < j:

    if l_1[i] != ".":
        i += 1
        continue

    
    if l_1[j] == ".":
         j -= 1
         continue

    l_1[i], l_1[j] = l_1[j], l_1[i]
    
    i+=1
    j-=1


count1 = 0
for idx, n in enumerate(l_1):
    if n == ".":
        break
    count1 += idx * int(n)