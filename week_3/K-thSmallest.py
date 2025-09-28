def select(A, k):
    assert 1 <= k <= len(A)
    if len(A) == 1:
        return A[0]
    p = choose_pivot(A)                         # len(A) = 1 이면 원소 반환
    A_less = [x for x in A if x < p]            # pivot 기준으로 list 나누기
    A_greater = [x for x in A if x > p]
    if len(A_less) == k - 1:
        return p
    elif len(A_less) > k - 1:
        return select(A_less, k)
    else:
        return select(A_greater, k - len(A_less) - 1)

def choose_pivot(A):
# Base case: if small enough, just sort and return median
    if len(A) <= 5:
        return sorted(A)[len(A) // 2]
# Step 1: Divide A into groups of 5
    groups = [A[i:i+5] for i in range(0, len(A), 5)]
# Step 2: Sort each group and collect their medians
    medians = [sorted(group)[len(group) // 2] for group in groups]
# Step 3: Recursively find the median of the medians
    return select(medians, k=(len(medians)+1)//2)

A = [13, 5, 2, 8, 9, 4, 7, 1, 6, 3, 10, 12, 11, 15, 14]
print(select(A, 4))