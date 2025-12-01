coins = [1, 5, 10, 21, 25]
INF = float("inf")
cost = 62
arr = [INF for _ in range(cost + 1)]
arr[0] = 0
usedCoin = [0 for _ in range(cost + 1)]
for i in range(1, cost + 1):
    for coin in coins:
        if i - coin < 0:
            continue

        temp = arr[i - coin] + 1
        if arr[i] > temp:
            arr[i] = temp
            usedCoin[i] = coin

print(arr)
print(usedCoin)

t = cost
answer = []
while t !=0:
    answer.append(usedCoin[t])
    t -=usedCoin[t]
    
print(answer)