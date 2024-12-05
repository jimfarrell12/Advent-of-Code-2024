import re

with open("input_day4.txt") as file:
    data = file.read()

words = ["SMSM", "SSMM", "MMSS", "MSMS"]
i = data.index("\n") - 1

ans = 0

for word in words:
    pattern = "(?s)(?=%%s.%%s.{%d}A.{%d}%%s.%%s)" % (i, i) % tuple(word)
    matches = re.findall(pattern, data)
    count = len(matches)
    ans += count

print(ans)
