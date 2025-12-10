import sys

input = sys.stdin.readline

INF = float("inf")

l, n = list(map(int, input().split()))

spots = list(map(int, input().split()))
spots = [0] + spots + [l]

n = len(spots)

arr = [[0] * n for _ in range(n)]

for length in range(2, n):

    for i in range(0, n - length):
        j = i + length
        minCost = INF
        for k in range(i + 1, j):
            cost = arr[i][k] + arr[k][j] + (spots[j] - spots[i])
            minCost = min(cost, minCost)
        arr[i][j] = minCost

for i in arr:
    print(i)
