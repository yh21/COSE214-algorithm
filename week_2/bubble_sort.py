# bubble sort
# # [ unsorted part | sorted part ]
# [5, 4, 1, 8, 7, 2, 6, 3|] # compare 5, 4 (swap) -> 4, 5
# [4, 5, 1, 8, 7, 2, 6, 3|] # compare 5, 1 (swap) -> 1, 5
# [4, 1, 5, 8, 7, 2, 6, 3|] # compare 5, 8 (do not swap) -> 5, 8
# [4, 1, 5, 8, 7, 2, 6, 3|] # compare 8, 7 (swap) -> 7, 8
# [4, 1, 5, 7, 8, 2, 6, 3|] # compare 8, 2 (swap) -> 2, 8
# [4, 1, 5, 7, 2, 8, 6, 3|] # compare 8, 6 (swap) -> 6, 8
# [4, 1, 5, 7, 2, 6, 8, 3|] # compare 8, 3 (swap) -> 3, 8
# [4, 1, 5, 7, 2, 6, 3 | 8] # the largest element 8 'bubble up' to the end!

# code of Bubble Sort
num = [5, 4, 1, 8, 7, 2, 6, 3]
for i in range(len(num) - 1):
    swapped = False
    for j in range(len(num) - i - 1):
        if num[j] > num[j + 1]:                         # >= 대신 > 써도 됨 (중복값 있을 때는 swap할 필요 없음)
            num[j], num[j + 1] = num[j + 1], num[j]
            swapped = True
    if not swapped:
        break                                           # 한 단계에서 swap이 일어나지 않았으면 이미 정렬된 상태임

print(num)