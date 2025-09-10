# bubble sort

# # Pass 1
# # [ unsorted part | sorted part ]
# [5, 4, 1, 8, 7, 2, 6, 3|] # compare 5, 4 (swap) -> 4, 5
# [4, 5, 1, 8, 7, 2, 6, 3|] # compare 5, 1 (swap) -> 1, 5
# [4, 1, 5, 8, 7, 2, 6, 3|] # compare 5, 8 (do not swap) -> 5, 8
# [4, 1, 5, 8, 7, 2, 6, 3|] # compare 8, 7 (swap) -> 7, 8
# [4, 1, 5, 7, 8, 2, 6, 3|] # compare 8, 2 (swap) -> 2, 8
# [4, 1, 5, 7, 2, 8, 6, 3|] # compare 8, 6 (swap) -> 6, 8
# [4, 1, 5, 7, 2, 6, 8, 3|] # compare 8, 3 (swap) -> 3, 8
# [4, 1, 5, 7, 2, 6, 3 | 8] # the largest element 8 'bubble up' to the end!

num = [5, 4, 1, 8, 7, 2, 6, 3]

for i in range(0, len(num) - 1):
    for j in range(0, len(num) - i - 1):
        if num[j] >= num[j + 1]:
            num[j], num[j + 1] = num[j + 1], num[j]

print(num)