import sys

def first(cycle):
    x = 2 * cycle - 1
    return x * x

def cycle(index):
    return (isqrt(index) + 1)//2

def length(cycle):
    return 8 * cycle

def sector(index):
    c = cycle(index)
    offset = index - first(c)
    n = length(c)
    return 4 * offset / n

def position(index):
    c = cycle(index)
    s = sector(index)
    offset = index - first(c) - s * length(c) // 4
    if s == 0: #north
        return -c, -c + offset + 1
    if s == 1: #east
        return -c + offset + 1, c
    if s == 2: #south
        return c, c - offset - 1
    # else, west
    return c - offset - 1, -c

def isqrt(x):
    """Calculates the integer square root of a number"""
    if x < 0:
        raise ValueError('square root not defined for negative numbers')
    n = int(x)
    if n == 0:
        return 0
    a, b = divmod(n.bit_length(), 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y

print(position(1))