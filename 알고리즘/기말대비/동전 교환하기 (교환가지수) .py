n = int(input())

coins = list(map(int, input().split()))
coins = coins[1:]

arr = [0] * (n+1)
arr[0] = 1
for coin in coins:
    for j in range(coin,n+1):
        arr[j] += arr[j-coin]
        
print(arr[n])