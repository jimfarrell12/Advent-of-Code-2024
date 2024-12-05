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

ans = 0

for i in range(len(a)):
    diff = abs(a[i] - b[i])
    ans += diff

print(ans)
