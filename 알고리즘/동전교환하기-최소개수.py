t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    data = list(map(int, input().split()))
    m = data[0]
    coins = data[1:]

    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, n + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    print(dp[n])
