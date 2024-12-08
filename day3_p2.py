import re

with open("input_day3.txt") as file:
    data = file.read()

pattern = r"(do\(\))|(don't\(\))|mul\(([0-9]+),([0-9]+)\)"
matches = re.findall(pattern, data)

ans = 0
active = True

for do, dont, a, b in matches:
    if do:
        active = True
    elif dont:
        active = False
    else:
        product = int(a) * int(b)
        ans += product * active

print(ans)
