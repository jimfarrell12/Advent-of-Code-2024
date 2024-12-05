import re 

with open("input_day3.txt") as file:
    data = file.read()

pattern = re.compile(r"mul\(([0-9]+),([0-9]+)\)")
matches = re.findall(pattern, data)

ans = 0

for pair in matches:
    product = int(pair[0]) * int(pair[1])
    ans += product

print(ans)
