def is_safe(nums):
    pairs = list(zip(nums, nums[1:]))
    increasing = all(a < b for a, b in pairs)
    decreasing = all(a > b for a, b in pairs)
    within_range = all(1 <= abs(a - b) <= 3 for a, b in pairs)
    return (increasing or decreasing) and within_range

def is_safe_dampener(nums):
    for i in range(len(nums)):
        alt_nums = nums[:]
        alt_nums.pop(i)
        if is_safe(alt_nums):
            return True  
    return False

with open("input_day2.txt", "r") as file:
    lines = file.read().splitlines()

safe_count = 0

for line in lines:
    nums = list(map(int, line.split()))
    if is_safe(nums) or is_safe_dampener(nums):
        safe_count += 1

print(safe_count)
