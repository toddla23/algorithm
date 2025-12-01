import sys
import heapq

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    INF = float("inf")
    arr = [[] for _ in range(n)]

    for _ in range(n):
        temp = list(map(int, input().split()))
        u = temp[0] - 1  # 0-based index
        m = temp[1]
        for j in range(m):
            v = temp[2 + 2 * j] - 1
            w = temp[2 + 2 * j + 1]
            arr[u].append((w, v))
            
    # print(arr)
            
    dist = [INF] * n
    dist[0] = 0
    toVisit = [(0,0)]
    parent = [-1] * n
    
    while toVisit:
        weight, toGo = heapq.heappop(toVisit)
        if dist[toGo] < weight:
            continue
        
        for weight1, toGo1 in arr[toGo]:
            # print(weight1, toGo1)

            
            if dist[toGo1] > dist[toGo] + weight1:
                dist[toGo1] = dist[toGo] + weight1
                parent[toGo1] = toGo
                heapq.heappush(toVisit, (dist[toGo1], toGo1))
    #             print(dist)
    #     print(toVisit)
    # print(dist)
    answer = 0
    for i in range(1, n):
        answer += dist[i] - dist[parent[i]]
        
    print(answer)