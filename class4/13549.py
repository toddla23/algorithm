from collections import deque

INF = float("inf")
maxnum = 100001


def bfs(n, k):

    arr = [INF] * maxnum
    isVisit = [False] * maxnum
    arr[n] = 0

    toVisit = deque()
    toVisit.append(n)
    while len(toVisit) != 0:
        visit = toVisit.popleft()
        if visit * 2 < maxnum:
            if arr[visit * 2] > arr[visit]:
                arr[visit * 2] = arr[visit]
                toVisit.appendleft(visit * 2)
        if visit +1 < maxnum:
            if arr[visit + 1] > arr[visit] + 1:
                arr[visit + 1] = arr[visit] + 1
                toVisit.append(visit + 1)
        if visit -1 >= 0:

            if arr[visit - 1] > arr[visit] + 1:
                arr[visit - 1] = arr[visit] + 1
                toVisit.append(visit - 1)
    
    
    print(arr[k])

    return 0


n, k = list(map(int, input().split(" ")))

bfs(n, k)
