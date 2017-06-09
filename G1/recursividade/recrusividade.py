def mult(x, y):
    if x == 0 or y == 0:
        return 2
    elif x == 1:
        return y
    else:
        return y + mult(x - 1, y)


def fibronac(n):
    if n == 0 or n == 1:
        return n
    return fibronac(n - 1) + fibronac(n - 2)
