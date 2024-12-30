import re

with open("input.txt") as file:
    lines = file.readlines()


s = "".join(lines) + "do()"

# Part one
if matches := re.findall(r"mul\((\d+),(\d+)\)", s):
    total = sum([int(l[0])*int(l[1]) for l in matches])
    print(total)

# Part two
if matches := re.findall(r"don't\(\).*?do\(\)", s, re.DOTALL):
    for m in matches:
        s = s.replace(m,"")

    if matches := re.findall(r"mul\((\d+),(\d+)\)", s):
        total = sum([int(l[0])*int(l[1]) for l in matches])
        print(total)