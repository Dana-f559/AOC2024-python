from functools import cache
from math import floor, log10
with open("inputs/01.txt", "r") as file:
        inp = file.read()


line = inp.splitlines()[0]

line = [int(l) for l in line.split(" ")]
blinks = 75

@cache
def next_stone(stone: int) -> tuple:
    if stone == 0:
        return 1
    
    if (l := floor(log10(stone)) + 1) % 2 == 0:
        return (int(stone // 10 ** (l/2)),int(stone % 10 ** (l/2)))
    
    return stone * 2024

@cache
def count_stones(stone: int) -> int:
    if stone == 0:
        return 1
    
    if (floor(log10(stone)) + 1) % 2 == 0:
        return 2
    
    return 1

@cache
def sab(stone, blinks):
    if blinks == 1:
        return count_stones(stone)
    
    else:
        if stone == 0:
            return sab(next_stone(stone), blinks - 1)
        
        if isinstance(st := next_stone(stone), tuple):
            return sab(st[0], blinks-1) + sab(st[1], blinks-1)

        return sab(stone*2024, blinks - 1)


count = 0
for n in line:
    count += sab(n, blinks)

print(count)