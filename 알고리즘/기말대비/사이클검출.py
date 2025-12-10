def union(x, y, arr):
    arr[y] = arr[x]


t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))

    arr = [i for i in range(n+1)]

    answer = 0
    for _ in range(m):
        u, v = list(map(int, input().split()))
        if arr[u] == arr[v]:
            answer = 1
        union(u, v, arr)
        
        
        # print(arr)
    print(answer)
