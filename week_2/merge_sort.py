def merge_sort(A):
    n = len(A)
    if n <= 1:
        return A
    L = merge_sort(A[:n//2])
    R = merge_sort(A[n//2:])
    return merge(L, R)

def merge(L, R):
    i = j = 0
    S = []
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            S.append(L[i])
            i += 1
        else:
            S.append(R[j])
            j += 1
    while i < len(L):
        S.append(L[i])
        i += 1
    while j < len(R):
        S.append(R[j])
        j += 1
    return S

num = [6, 5, 12, 10, 9, 1]
print(merge_sort(num))