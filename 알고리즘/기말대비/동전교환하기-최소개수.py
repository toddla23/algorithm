t = int(input())
for _ in range(t):
    n = int(input().strip())
    data = list(map(int, input().split()))
    data = data[1:]

    arr = [0 for _ in range(n+1)]

    for cost in range(1,n+1):
        minCount = float('inf')
        for coin in data:
            if cost-coin < 0:
                continue
            minCount = min(minCount, arr[cost-coin] + 1)
        arr[cost] = minCount

    print(arr)