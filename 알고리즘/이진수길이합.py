import sys
import math


def calc(n: int) -> int:
    if n == 0:
        return 0
    lgn = n.bit_length()-1

    result = n * lgn + n + lgn - 2 ** (lgn + 1) + 2

    return result


input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    print(calc(n))
