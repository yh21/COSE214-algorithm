# Code of Lomuto Partition Algorithm

nums = [3, 8, 2, 5, 1, 4, 7, 6]

def partition(A, left, right):
    pivot = A[left] # pivot을 첫 번째 element로 설정
    i = left + 1
    for j in range(left + 1, right +1):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[left], A[i - 1] = A[i - 1], A[left]
    return i - 1 # pivot의 index return

print(partition(nums, 0, len(nums) - 1), nums)

# [3, 8, 2, 5, 1, 4, 7, 6] i = 1, j = 1 no swap | 8 > 3
# [3, 2, 8, 5, 1, 4, 7, 6] i = 1, j = 2 swap 8, 2 and i += 1
# [3, 2, 8, 5, 1, 4, 7, 6] i = 2, j = 3 no swap
# [3, 2, 1, 5, 8, 4, 7, 6] i = 2, j = 4 swap 8, 1 and i += 1
# .
# .
# no swap
# swap A[i - 1](A[2]), A[left](A[0])
# [1, 2, 3, 5, 8, 4, 7, 6]