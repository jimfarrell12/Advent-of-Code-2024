with open("input_day2.txt", "r") as file:
    lines = file.read().splitlines()

safe_count = 0

for line in lines:
    nums = list(map(int, line.split()))
    pairs = list(zip(nums, nums[1:]))

    increasing = all(a < b for a, b in pairs)
    decreasing = all(a > b for a, b in pairs)
    within_range = all(1 <= abs(a - b) <= 3 for a, b in pairs)

    is_safe = (increasing or decreasing) and within_range
    #print(f"{line}: {is_safe}")

    if is_safe:
        safe_count += 1

print(safe_count)
