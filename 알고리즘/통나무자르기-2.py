import sys

input = sys.stdin.readline


def calc(spot):
    n = len(spot)
    costs = [[0 for _ in range(n)] for _ in range(n)]

    for length in range(2, n):
        for i in range(0, n - length):
            j = i + length
            minCost = float("inf")
            for k in range(i + 1, j):
                cost = costs[i][k] + costs[k][j] + (spot[j] - spot[i])
                if cost < minCost:
                    minCost = cost
            costs[i][j] = minCost
    for i in costs:
        print(i)

    return costs[0][n-1]


# n = int(input())
# for _ in range(n):
#     l, t = list(map(int, input().split()))
#     arr = list(map(int, input().split()))
#     spot = [0] + arr + [l]
#     print(calc(spot))
calc([0,2,6,7,10])