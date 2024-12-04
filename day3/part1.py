import re

total = 0

with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
        match = re.findall(r"mul\(\d{1,3}\,\d{1,3}\)", line)
        for m in match:
            m = m.replace("mul(", "").replace(")", "").split(",")
            total += int(m[0]) * int(m[1])

print(total)