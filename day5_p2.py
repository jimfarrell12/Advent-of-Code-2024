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
incorrect_updates = []

correct_sum = 0
corrected_sum = 0

def is_ordered(update, map):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            x, y = update[i], update[j]
            if (x, y) in map and not map[(x, y)]:
                return False
    return True


def correct_update(update, map):
    for i in range(len(update)):
        for j in range(len(update) - 1):
            a, b  = update[j], update[j + 1]
            if (a, b) in map and not map[(a, b)]: 
                update[j], update[j + 1] = update[j + 1], update[j]
    return update


for update in updates:
    if is_ordered(update, map):
        correct_updates.append(update)
        middle_i = len(update) // 2
        middle_num = update[middle_i]
        correct_sum += middle_num
    else:
        incorrect_updates.append(update)
        corrected_sequence = correct_update(update.copy(), map)
        corrected_middle_i = len(corrected_sequence) // 2
        corrected_middle_num = corrected_sequence[corrected_middle_i]
        corrected_sum += corrected_middle_num


print(correct_sum, corrected_sum)
