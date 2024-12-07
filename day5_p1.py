with "input_day5.txt".open() as file:
    nums = file.read().split()

rules = []
updates = []

rule_char = "|"
update_char = ","


for num in nums:
    if rule_char in num:
        rule = list(map(int, num.split(rule_char)))
        rules.append(rule)
    else:
        update = list(map(int, num.split(update_char)))
        updates.append(update)

map = {}

for x, y in rules:
    map[(x, y)] = True
    map[(y, x)] = False

correct_updates = []
#middle_nums = []
ans = 0

for update in updates:
    in_order = True 

    for i in range(len(update) - 1):
        x, y = update[i], update[i + 1]

        if (x, y) in map and map[(y, x)]:
            in_order = False
            break

    if in_order:
        correct_updates.append(update)
        middle_i = len(update) // 2
        middle_num = update[middle_i]
        #middle_nums.append(middle_num)
        ans += middle_num

print(ans)
