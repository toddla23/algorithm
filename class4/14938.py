INF = float("inf")

n, m, r = list(map(int, input().split()))

t = list(map(int, input().split()))


arr = [[INF] * n for _ in range(n)]

for i in range(n):
    arr[i][i] = 0

for i in range(r):
    a, b, l = list(map(int, input().split()))
    arr[a - 1][b - 1] = l
    arr[b - 1][a - 1] = l


for k in range(n):
    for a in range(n):
        for b in range(n):
            arr[a][b] = min(arr[a][b], arr[a][k] + arr[k][b])

answer = 0
for i in range(n):
    temp = 0
    for j in range(n):
        if arr[i][j] <= m:
            temp += t[j]
    answer = max(answer, temp)

print(answer)
