X = int(input())
Y = int(input())

def karatsuba(x, y):
    x_str = str(x)
    y_str = str(y)

    n_digit = max(len(x_str), len(y_str))
    x_str = x_str.zfill(n_digit)
    y_str = y_str.zfill(n_digit)

    if n_digit == 1:
        return x * y                    # n = 1이면 곱을 return
    
    m = n_digit // 2
    split = n_digit - m

    a = int(x_str[:split])
    b = int(x_str[split:])
    c = int(y_str[:split])
    d = int(y_str[split:])

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    t = karatsuba(a + b, c + d) - ac - bd

    return ac * (10 ** (2 * m)) + t * (10 ** m) + bd

print(karatsuba(X, Y))