import re

with open("inputs/01.txt", "r") as file:
    inp = file.read()

lines = inp.splitlines()

rgs = re.findall(r"\d+", lines[0]+lines[1]+lines[2])
operands = [0, 1, 2, 3, int(rgs[0]), int(rgs[1]), int(rgs[2]), 7]
inst = [int(i) for i in lines[4] if i.isdigit()]
A, B, C = 4, 5, 6

full = ""

cur_pos = 0
while cur_pos < len(inst):

    opcode = inst[cur_pos]
    operand = inst[cur_pos+1]

    if opcode in {0, 6, 7}:
        val = {0: 4, 6: 5, 7: 6}
        operands[val[opcode]] = int(operands[A] / (2 ** operands[operand]))

    if opcode == 1:
        operands[B] = int(operands[B] ^ operand)
 
    if opcode == 2:
        operands[B] = int(operands[operand] % 8)

    if opcode == 3 and operands[A] != 0:
        cur_pos = operand
        continue

    if opcode == 4:
        operands[B] = int(operands[B] ^ operands[C])

    if opcode == 5:
        full += f"{int(operands[operand] % 8)},"
    
    cur_pos += 2

print(full)
