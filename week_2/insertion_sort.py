# insertion sort

# [_, _, _, _]
# ------------
# [5, _, _, _] # Insert 5
# ------------
# [_, 5, _, _] # 5 > 4. Shift 5 to the right
# [4, 5, _, _] # Insert 4
# ------------
# [4, _, 5, _] # 5 > 2. Shift 5 to the right
# [_, 4, 5, _] # 4 > 2. Shift 5 to the right
# [2, 4, 5, _] # Insert 2

num = [5, 4, 1, 8, 7, 2, 6, 3]

for i in range(1, len(num)):
    current  = num[i]
    j = i - 1
    while j >= 0 and num[j] > current:
        num[j + 1] = num[j]
        j -= 1
    num[j + 1] = current

print(num)