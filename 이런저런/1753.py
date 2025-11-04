import sys
import heapq

input = sys.stdin.readline
INF = float("inf")


def calc(result, start, graph):
    q = []
    heapq.heappush(q, (0, start))
    result[start] = 0

    while q:
        cost, start = heapq.heappop(q)

        if result[start] < cost:
            continue

        for end, cost1 in graph[start]:
            cost2 = cost + cost1
            if cost2 < result[end]:
                result[end] = cost2
                heapq.heappush(q, (cost2, end))

    return


n, t = map(int, input().split(" "))

start = int(input())
start = start - 1
result = [INF] * n
result[start] = 0

graph = [[] for _ in range(n)]

for _ in range(t):
    s, e, c = map(int, input().split(" "))
    graph[s - 1].append((e - 1, c))

calc(result, start, graph)
for i in range(n):
    if result[i] == INF:
        print("INF")
    else:
        print(result[i])

