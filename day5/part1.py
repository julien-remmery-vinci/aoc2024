import math

orders = []
updates = []

order = True

total = 0

def is_valid(update):
    for num in update:
        for order in orders:
            if num in order and order[0] == num and order[1] in update and update.index(num) > update.index(order[1]):
                    return False
    return True


with open("input.txt") as f:
    for line in f:
        line = line.replace("\n", "")
        if "|" in line:
            orders.append(list(map(int, line.split("|"))))
        elif "," in line:
            updates.append(list(map(int, line.split(","))))
    for update in updates:
        if is_valid(update):
            total += update[math.floor(len(update)/2)]

print(total)