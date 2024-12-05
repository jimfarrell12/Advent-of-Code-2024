with open("input.txt", "r") as file:
    lines = file.read().splitlines()

a = []
b = []

for line in lines:
    nums = list(map(int, line.split()))
    a.append(nums[0])
    b.append(nums[1])

ans = 0

for num in a:
    ans += num * b.count(num)

print(ans)
