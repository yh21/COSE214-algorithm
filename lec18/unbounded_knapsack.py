def unbounded_knapsack(W, items):
    # W (int) : Maximum Capacity
    # items (list of tuples) : Each tupleis (weight, value)
    n = len(items)
    K = [0] * (W + 1)
    for x in range(1, W + 1):
        for i in range(n):
            w, v = items[i]
            if w <= x:
                candidate = K[x - w] + v
                if candidate > K[x]:
                    K[x] = candidate
    return K[W]