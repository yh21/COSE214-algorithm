import random

def quicksort(A, left, right):
    if left >= right:
        return A
    pivot_index = random.randint(left, right) # randompivot
    A[left], A[pivot_index] = A[pivot_index], A[left]
    new_pivot_index = partition(A, left, right)
    quicksort(A, left, new_pivot_index - 1)
    quicksort(A, new_pivot_index + 1, right)

def partition(A, left, right):
    pivot = A[left]
    i = left + 1
    for j in range(left + 1, right + 1):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[left], A[i - 1] = A[i - 1], A[left]
    return i - 1

A = [8, 2, 6, 5, 4, 7, 1, 3]
quicksort(A, 0, len(A) - 1)
print(A)