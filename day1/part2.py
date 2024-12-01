left = []
right = []

with open('input.txt') as f:
    for line in f:
        split = line.split(" ")
        left.append(int(split[0]))
        right.append(int(split[3]))


total = 0

while left and right:
    first = left[0]
    nb = right.count(first)

    left.remove(first)

    total += first * nb

print(total)