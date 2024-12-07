with "input_day5.txt".open() as file:
    nums = file.read().split()

rules = []
updates = []

for num in nums:
    if "|" in num:
        rule = list(map(int, num.split("|")))
        rules.append(rule)
    else:
        update = list(map(int, num.split(",")))
        updates.append(update)

map = {}

for x, y in rules:
    map[(x, y)] = True
    map[(y, x)] = False

correct_updates = []
ans = 0

def is_ordered(update, map):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            x, y = update[i], update[j]
            if (x, y) in map and not map[(x, y)]:
                return False
    return True

for update in updates:
    if is_ordered(update, map):
        correct_updates.append(update)
        middle_i = len(update) // 2
        middle_num = update[middle_i]
        ans += middle_num

print(ans)
