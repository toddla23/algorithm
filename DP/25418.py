def solve():
    A, K = map(int, input().split())
    INF = float('inf')
    dp = [INF] * (K + 1)
    dp[A] = 0

    for i in range(A + 1, K + 1):
        dp[i] = dp[i - 1] + 1
        if i % 2 == 0 and i // 2 >= A:
            dp[i] = min(dp[i], dp[i // 2] + 1)

    print(dp[K])

if __name__ == "__main__":
    solve()