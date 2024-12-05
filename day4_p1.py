import re

with open("input_day4.txt") as file:
    data = file.read()

words = ["XMAS", "SAMX"]
i = data.index("\n")
offsets = [0, i+1, i, i-1]

ans = 0

for word in words:
    for offset in offsets:
        pattern = "(?s)(?=%s)" % (".{%d}" % offset).join(word)
        matches = re.findall(pattern, data)
        count = len(matches)
        ans += count

print(ans)
