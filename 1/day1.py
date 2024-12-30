list1 = []
list2 = []

with open('input2.txt', 'r') as file:
    # Read all lines from the file
    lines = file.readlines()

# Process each line
for line in lines:
    numbers = list(map(int, line.split()))
    
    list1.append(numbers[0])
    list2.append(numbers[1])

similarity = 0
for l in list1:
    n = list2.count(l)
    similarity += n*l

print(f"{similarity = }")

distance = 0
while list1:

    min1 = min(list1)
    list1.remove(min1)

    min2 = min(list2)
    list2.remove(min2)
    distance += abs(min1 - min2)


print(f"{distance = }")