# selection sort

# [|5, 4, 1, 8, 7, 2, 6, 3] # 1 is the smallest, swap with 5
# [1 | 4, 5, 8, 7, 2, 6, 3] # 2 is next smallest, swap with 4
# [1, 2 | 5, 8, 7, 4, 6, 3] # 3 is next, swap with 5
# [1, 2, 3 | 8, 7, 4, 6, 5] # 4 is next, swap with 8
# [1, 2, 3, 4 | 7, 8, 6, 5] # 5 is next, swap with 7
# [1, 2, 3, 4, 5 | 8, 6, 7] # 6 is next, swap with 8
# [1, 2, 3, 4, 5, 6 | 8, 7] # 7 is next, swap with 8
# [1, 2, 3, 4, 5, 6, 7 | 8] # Done!

num = [5, 4, 1, 8, 7, 2, 6, 3]

for i in range(0, len(num)):
    current = num[i]
    min_value = current
    for j in range(i + 1, len(num)):
        if num[j] < min_value:
            min_value = num[j]
            count = j
    if min_value != num[i]:
        num[count], num[i] = num[i], num[count]

print(num)