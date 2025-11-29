def zero_one_knapsack(W, items):
    # W (int) : Maximum Capacity
    # items (list of tuples) : Each tuple is (weight, value)
    n = len(items)
    K = [[0] * (n + 1) for _ in range(W + 1)]

    for j in range(1, n + 1):
        w, v = items[j - 1]
        for x in range(1, W + 1):
            K[x][j] = K[x][j - 1]
            if x >= w:
                K[x][j] = max(K[x][j], K[x - w][j - 1] + v)

    return K[W][n]