left = []
right = []

with open('input.txt') as f:
    for line in f:
        split = line.split(" ")
        left.append(int(split[0]))
        right.append(int(split[3]))


total = 0

while left and right:
    minLeft = min(left)
    minRight = min(right)

    left.remove(minLeft)
    right.remove(minRight)

    total += abs(minLeft - minRight)

print(total)