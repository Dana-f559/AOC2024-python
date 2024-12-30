import re
import numpy as np

with open("inputs/01.txt", "r") as file:
    inp = file.read()

lines = inp.splitlines()

extra_num = 10_000_000_000_000

def solve(button_A, button_B, prize):
    A = np.array([[int(button_A[0]), int(button_B[0])],
                [int(button_A[1]), int(button_B[1])]])
    B = np.array([int(prize[0])+extra_num, int(prize[1])+extra_num])

    try:
        x = np.linalg.solve(A, B)
        return (x[0], x[1]) 
    except np.linalg.LinAlgError:
        return (False)

sums = 0

for i in range(0, len(lines), 4):
    button_A = re.findall(r"\+(\d+)", lines[i])
    button_B = re.findall(r"\+(\d+)", lines[i+1])
    prize = re.findall(r"=(\d+)",lines[i+2])
    
    a, b = solve(button_A, button_B, prize)

    if round(a, 2).is_integer() and round(b, 2).is_integer():
        sums += round(a) * 3 + round(b)

print(sums)