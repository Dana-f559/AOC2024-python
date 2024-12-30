

def main():
    with open("input.txt") as file:
        lines = file.readlines()


    lines = [l.strip("\n").split(":") for l in lines]

    #! PART ONE
    # sums = 0
    # for l in lines:
    #     goal = int(l[0])
    #     ns = list(map(int, l[1].strip().split(" ")))
    #     if check_n_a(goal, ns):
    #         sums += goal

    # print(sums)

    #! PART TWO
    sums = 0
    for l in lines:
        goal = int(l[0])
        ns = list(map(int, l[1].strip().split(" ")))
        if check_n_b(goal, ns):
            sums += goal

    print(sums)
    
def check_n_b(goal:int, ns:list[int]) -> bool:

    # go though the loop to check all posibilities
    for i in range(3**(len(ns)-1)):
        val = bin(i).replace("0b","")
        base3_value = ""
        n = i
        while n > 0:
            base3_value = str(n % 3) + base3_value
            n //= 3
        val = base3_value.zfill(len(ns)-1)

        cur = ns[0]
        for j in range(len(ns)-1):
            
            if val[j] == "0":
                cur += ns[j+1]
            elif val[j] == "1":
                cur *= ns[j+1]
            else:
                cur = int(str(cur) + str(ns[j+1]))
        if cur == goal:
            return True
        
    return False


def check_n_a(goal:int, ns:list[int]) -> bool:

    # go though the loop to check all posibilities
    for i in range(2**(len(ns)-1)):
        val = bin(i).replace("0b","")
        val = "0" * (len(ns)-1 - len(val)) + val

        cur = ns[0]
        for j in range(len(ns)-1):
            
            if val[j] == "0":
                cur += ns[j+1]
            else:
                cur *= ns[j+1]

        if cur == goal:
            return True
        
    return False

main()