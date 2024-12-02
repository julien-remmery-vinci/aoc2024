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

def is_safe_dampener(line):
    if(is_safe(line)):
        return True
    for i in range(len(line)):
        modified = line[:i] + line[i+1:]
        if(is_safe(modified)):
            return True
    return False

total = 0

with open("input.txt") as f:
    for line in f:
        line = line.split()
        if is_safe_dampener(line):
            total += 1
            
print(total)