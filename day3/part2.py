import re

total = 0

enabled = ""

def remove_disabled(line):
    tmp = line.split("don't()")

    enabled = tmp[0]
    enabled += tmp[1].split("do()")[1]
    return enabled

with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
        match = re.search(r"don\'t\(\)([^d]*(?:d(?!o\().)*?)do\(\)", line)

        while match:
            line = line.replace(match.group(), "")
            match = re.search(r"don\'t\(\)([^d]*(?:d(?!o\().)*?)do\(\)", line)

        if "don't" in line:
            line = re.sub(r"don\'t\(\).*", "", line)

        match = re.findall(r"mul\(\d{1,3}\,\d{1,3}\)", line)
        for m in match:
            m = m.replace("mul(", "").replace(")", "").split(",")
            total += int(m[0]) * int(m[1])

print(total)