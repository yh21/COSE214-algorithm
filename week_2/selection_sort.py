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
    min_value = num[i]
    for j in range(i + 1, len(num)):
        if num[j] < min_value:
            min_value = num[j]
            count = j
    if min_value != num[i]:
        num[count], num[i] = num[i], num[count]

print(num)

# count가 정의 안될 수도 있음
# min_idx가 i인 경우 자체 swap도 가능

num = [5, 4, 1, 8, 7, 2, 6, 3]

for i in range(len(num) - 1): # len(num) - 1 번만 정렬해도 맨 마지막건 자동으로 정렬됨
    min_idx = i
    for j in range(i + 1, len(num)):
        if num[j] < num[min_idx]:
            min_idx = j
    num[i], num[min_idx] = num[min_idx], num[i]

print(num)