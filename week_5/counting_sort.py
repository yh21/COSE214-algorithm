# counting sort
# bucket sort랑은 다름!!!!!

nums = [1, 7, 9, 2, 6, 7, 4, 8]
lenn = len(nums)
max_val = max(nums)
count = [0] * (max_val + 1)

for i in range(lenn):
    count[nums[i]] += 1

sorted_nums = []
for i in range(max_val + 1):
    sorted_nums.extend([i] * count[i])

print(sorted_nums)