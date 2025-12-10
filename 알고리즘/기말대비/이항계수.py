arr = [[1] * 101 for _ in range(101)]

for k in range(101):
    for n in range(101):
        if k == 0 or k == n:
            continue

        if 0 < k < n:
            arr[n][k] = (arr[n - 1][k] + arr[n - 1][k - 1]) % 1000000007
t = int(input())
for _ in range(t):
    a, b = list(map(int, input().split()))

    print(arr[a][b])
