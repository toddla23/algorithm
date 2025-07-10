import sys
import heapq

input = sys.stdin.readline
maximum = float("inf")

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))  # u → v 로 가는 비용 w


# print(graph)

start, end = map(int, input().split())


dist = [maximum] * (n + 1)
dist[start] = 0

# print(dist)

heap = [(0, start)]

while heap:
    cost, city = heapq.heappop(heap)
    
    if dist[city] < cost:
        continue
    
    for nextCity, nextCost in graph[city]:
        total = cost + nextCost
        if(total < dist[nextCity]):
            dist[nextCity] = total
            heapq.heappush(heap, (total, nextCity))
            
print(dist[end])