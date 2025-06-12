import sys

input = sys.stdin.readline
INF = 1e9

n, m = map(int, input().split(" "))

arr = [[INF for i in range(n + 1)] for i in range(n + 1)]


for _ in range(m):
    a, b = map(int, input().split(" "))
    arr[a][b] = 1
    arr[b][a] = 1

for i in range(1, n + 1):
    arr[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])


# for i in arr:
#     print(i)


min_sum = INF
answer = 0

for i in range(1, n + 1):
    total = sum(arr[i][1:])
    if total < min_sum:
        min_sum = total
        answer = i

print(answer)
