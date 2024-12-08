import re 

with open("input_day3.txt") as file:
    data = file.read()

pattern = r"mul\(([0-9]+),([0-9]+)\)"
matches = re.findall(pattern, data)

ans = 0

for match in matches:
    nums = list(map(int, match))
    product = nums[0] * nums[1]
    ans += product

print(ans)
