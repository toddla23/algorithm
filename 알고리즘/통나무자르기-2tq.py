import sys

input = sys.stdin.readline


def calc(log, arr):
    spot = [0] + [arr] + [log]
    n = len(spot)
    costs = [[0 for _ in range(n)] for _ in range(n)]
    for length in range(n):
        for i in range(0,n-length):
            j = i+length

    return 0


# n = int(input())
# for _ in range(n):
# l, t = list(map(int, input().split(" ")))
# arr = list(map(int, input().split(" ")))
# calc(l, arr)

calc(10, [2, 6, 7])
