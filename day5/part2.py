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

def sort_both(first, second):
    for order in orders:
        if first in order and second in order:
            return order[0], order[1]

def fix(update):
    i = 0
    while i < len(update)-1:
        first, second = sort_both(update[i], update[i+1])
        if first != update[i]:
            update[i] = first
            update[i+1] = second
            i = 0
        else:
            i += 1
    return update

with open("input.txt") as f:
    for line in f:
        line = line.replace("\n", "")
        if "|" in line:
            orders.append(list(map(int, line.split("|"))))
        elif "," in line:
            updates.append(list(map(int, line.split(","))))
    for update in updates:
        if not is_valid(update):
            update = fix(update)
            total += update[math.floor(len(update)/2)]

print(total)