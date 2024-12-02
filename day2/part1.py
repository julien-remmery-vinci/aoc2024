def is_safe(line):
    increasing = False
    decreasing = False
    last = int(line[0])
    for i in range(1, len(line)):
        current = int(line[i])
        if not current > last:
            break
        if current - last > 3:
            break
        if i == len(line) - 1:
            increasing = True
        last = current
    last = int(line[0])
    for i in range(1, len(line)):
        current = int(line[i])
        if not current < last:
            break
        if last - current > 3:
            break
        if i == len(line) - 1:
            decreasing = True
        last = current
    return increasing or decreasing

total = 0

with open("input.txt") as f:
    for line in f:
        line = line.split()
        if is_safe(line):
            total += 1
            
print(total)