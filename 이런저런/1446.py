import sys
import heapq

input = sys.stdin.readline

INF = float("inf")


n, d = map(int, input().split(" "))

graph = {}

for _ in range(n):
    start, end, distance = map(int, input().split(" "))
    if end > d:
        continue
    if start in graph.keys():
        graph[start].append((end, distance))
    else:
        graph[start] = [(end, distance)]

dist = [INF for _ in range(d + 1)]
dist[0] = 0

toGo = [(0, 0)]

while toGo:
    end, distance = heapq.heappop(toGo)

    if distance > dist[end]:
        continue
    
    if end < d and distance + 1 < dist[end + 1]:
        heapq.heappush(toGo, (end + 1, distance + 1))
        dist[end+1] = distance + 1

    if end in graph.keys():
        for goLocation, goCost in graph[end]:
            total = distance + goCost
            if total < dist[goLocation]:
                dist[goLocation] = total
                heapq.heappush(toGo, (goLocation, total))


# print(dist)
print(dist[d])
