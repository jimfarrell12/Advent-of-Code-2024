with open("input.txt", "r") as file:
    lines = file.read().splitlines()

a = []
b = []

for line in lines:
    a.append(line.split()[0])
    b.append(line.split()[1])

ans = 0

for num in a:
    ans += int(num) * b.count(num)

print(ans)
