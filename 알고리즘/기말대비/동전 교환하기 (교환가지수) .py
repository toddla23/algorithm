t = int(input())
for _ in range(t):
    n = int(input())

    coins = list(map(int, input().split()))
    coins = coins[1:]

    arr = [0] * (n+1)
    arr[0] = 1
    for coin in coins:
        for i in range(coin, n+1):
            arr[i] += arr[i-coin]
            
    print(arr[n])