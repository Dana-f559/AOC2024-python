with open("input.txt") as file:
    lines = file.readlines()

lines = [list(map(int, l.split())) for l in lines]
count = 0

def check_if_safe(report: list[int], direction:bool) -> bool:
    safe = True
    for x in range(len(report) - 1):
        # check if the direction of the levels are the same as at the start
        d = True if report[x] - report[x + 1] < 0 else False
        
        if direction != d:
            safe = False

        # if the difference between the levels is not 1, 2 or 3, return false
        if (abs(report[x] - report[x + 1]) not in [1,2,3]):
            safe = False

    return safe

# PART ONE
for report in lines:
    # true if accending, false is deccending
    direction = False if report[1] - report[0] < 0 else True

    # part one
    if check_if_safe(report, direction):
        count += 1
    
# PART TWO
count_2 = 0
for report in lines:
    safe = False

    for i in range(len(report)):

        x = report.pop(i)

        direction = False if report[1] - report[0] < 0 else True

        if check_if_safe(report,direction):
            
            safe = True

        report.insert(i, x)
    
    if safe:
        count_2 += 1