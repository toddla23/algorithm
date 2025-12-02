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
            
    dist = [INF] * n # 0에서 n까지의 경로 가중치
    dist[0] = 0
    toVisit = [(0,0)] #(0,0) 부터 방문
    parent = [-1] * n
    
    while toVisit:
        weight, toGo = heapq.heappop(toVisit)
        if dist[toGo] < weight: # 0에서 togo까지가 예전에 했던거보다 많으면 할필요없음
            continue
        
        for weight1, toGo1 in arr[toGo]: # 다음 경로 탐색
            # print(weight1, toGo1)

            
            if dist[toGo1] > dist[toGo] + weight1: # 예전에 갔던 경로 > 예전에 togo 까지 간거 + 앞으로 갈거
                dist[toGo1] = dist[toGo] + weight1 # 갱신
                parent[toGo1] = toGo # 부모 저장
                heapq.heappush(toVisit, (dist[toGo1], toGo1)) #(0에서 togo1까지 간거 ,다음 갈거)
    #             print(dist)
    #     print(toVisit)
    # print(dist)
    answer = 0
    for i in range(1, n):
        answer += dist[i] - dist[parent[i]]
        
    print(answer)