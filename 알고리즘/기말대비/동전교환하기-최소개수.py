INF = float("inf")
t = int(input())
for _ in range(t):
    cost = int(input())
    temp = list(map(int, input().split()))
    coins = temp[1:]

    costs = [0 for _ in range(cost + 1)]

    for i in range(1, cost + 1):
        minCost = INF
        for coin in coins:
            if i - coin < 0:
                continue
            minCost = min(minCost, costs[i - coin] + 1)
        costs[i] = minCost
        
    print(costs[cost])
