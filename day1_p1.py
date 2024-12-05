with open("input.txt", "r") as file:
    lines = file.read().splitlines()

a = []
b = []

for line in lines:
    nums = list(map(int, line.split()))
    a.append(nums[0])
    b.append(nums[1])

a.sort()
b.sort()

dists = []

for i in range(len(a)):
    dist = abs(a[i] - b[i])
    dists.append(dist)

total_dist = sum(dists)

print(total_dist)
