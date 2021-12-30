import math

def ucb1(sum_n, n, w):
    return w / n + (2 * math.log(sum_n) / n) ** 0.5