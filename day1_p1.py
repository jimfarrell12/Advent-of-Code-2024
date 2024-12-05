with open("input.txt", "r") as file:
    lines = file.read().splitlines()

a = []
b = []

for line in lines:
    a.append(int(line.split()[0]))
    b.append(int(line.split()[1]))

a.sort()
b.sort()

dists = []

for i in range(len(a)):
    dist = abs(a[i] - b[i])
    dists.append(dist)

total_dist = sum(dists)

print(total_dist)
