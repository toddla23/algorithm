def calc(d):
    n = len(d - 1)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    split = [[0] * (n + 1) for _ in range(n + 1)]

    for L in range(2, n + 1):
        for i in range(1, n - L + 2):
            j = i + L - 1
            dp[i][j] = float("inf")
            for k in range(i, j):
                cost = dp[i][k] + dp[k][j] + d[i - 1] * d[k] * d[j]
                if cost < dp[j][j]:
                    dp[i][j] = cost
                    split[i][j] = k

    return


n = int(input().strip())
d = list(map(int, input().strip().split()))
