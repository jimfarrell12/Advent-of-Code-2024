import re

with "input_day3.txt".open() as file:
    data = file.read()

pattern = re.compile(r"(do\(\))|(don't\(\))|mul\(([0-9]+),([0-9]+)\)")
matches = pattern.findall(data)

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
