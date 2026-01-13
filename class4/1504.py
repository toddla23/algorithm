import sys
import heapq


def calc(start, end, arr):
    visit = [False] * (n + 1)
    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        cost, now = heapq.heappop(heap)
        # print(now, cost)
        if visit[end]:
            break
        if visit[now]:
            continue
        visit[now] = True

        for i in range(1, n+1):
            
            if visit[i] or arr[start][now] + arr[now][i] == INF:
                continue

            if arr[start][i] >= arr[start][now] + arr[now][i]:
                arr[start][i] =  arr[start][now] + arr[now][i]
                heapq.heappush(heap, (arr[start][i], i))
            # print(heap)
        # print(arr[start])
    return arr[start][end]


input = sys.stdin.readline
INF = float("inf")

n, e = list(map(int, input().split()))

arr = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(e):
    a, b, c = list(map(int, input().split()))
    arr[a][b] = c
    arr[b][a] = c

for i in range(n + 1):
    arr[i][i] = 0

v1,v2 = list(map(int, input().split()))
answer = min(calc(1,v1,arr) + calc(v2,n,arr), calc(1,v2,arr) + calc(v1,n,arr)) + calc(v1,v2,arr)
if (answer == INF):
    print(-1)
else:
    print(answer)