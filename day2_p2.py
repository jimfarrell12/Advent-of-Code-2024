def pair_nums(nums):
    return list(zip(nums, nums[1:]))

def is_safe(pairs):
    increasing = all(a < b for a, b in pairs)
    decreasing = all(a > b for a, b in pairs)
    within_range = all(1 <= abs(a - b) <= 3 for a, b in pairs)
    return (increasing or decreasing) and within_range

with open("input_day2.txt", "r") as file:
    lines = file.read().splitlines()

safe_count = 0

for line in lines:
    nums = list(map(int, line.split()))
    pairs = pair_nums(nums)
    safe = is_safe(pairs)

    if not safe:
        for i in range(len(nums)):
            alt_nums = nums[:]
            alt_nums.pop(i)
            alt_pairs = pair_nums(alt_nums)
            alt_safe = is_safe(alt_pairs)

            if alt_safe:
                safe = True
                break

    if safe:
        safe_count += 1

print(safe_count)
