import sys

input = sys.stdin.readline


def calc(spot):
    n = len(spot)
    costs = [[0 for _ in range(n)] for _ in range(n)]

    for length in range(2, n):  # 인덱스 간의 간격
        for i in range(0, n-length): # 시작지점 = 0 ~ 전체 간격 -자를간격
            j = i+length # 끝지점 = 시작지점 + 자를 간격
            cost = float('inf')
            for k in range(i+1, j):
                cost = min(cost, costs[i][k] + costs[k][j] + (spot[j]-spot[i]))
            costs[i][j] = cost
    for i in costs:
        print(i)


n = int(input())

for _ in range(n):
    l, t = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    spot = [0] + arr + [l]
    result = calc(spot)
