with open("input.txt") as file:
    lines = [l.strip("\n") for l in file.readlines()]

rules = [tuple(map(int,l.split("|"))) for l in lines[:lines.index("")]]
pages = [list(map(int,l.split(","))) for l in lines[lines.index("")+1:]]

pages_notsafe = []
m_sum = 0
m_sum_inc = 0

#! PART ONE
for p in pages:
    safe = True
    for t in range(1, len(p)):
        n1 = p[t-1]
        n2 = p[t]
        if (n1, n2) not in rules:

            safe = False

    if safe:
        m_sum += p[len(p)//2]
    if not safe:
        pages_notsafe.append(p)


#! PART TWO
for p in pages_notsafe:
    safe = False
    while not safe:
        
        safe = True

        for t in range(1, len(p)):
            n1 = p[t-1]
            n2 = p[t]

            if (n1, n2) not in rules:
                # Switch the elements in the array
                p[t-1], p[t] = p[t], p[t-1]
                safe = False  # Not safe, need another pass

    
    m_sum_inc += p[len(p)//2]

print(m_sum_inc)