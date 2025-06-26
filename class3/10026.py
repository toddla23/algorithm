import sys
from collections import deque

input = sys.stdin.readline


def dfs1(arr: list, x: int, y: int):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if (0 <= ax < n) and 0 <= ay < n:
                if not isVisited1[ax][ay] and arr[x][y] == arr[ax][ay]:
                    isVisited1[ax][ay] = True
                    queue.append((ax, ay))


def dfs2(arr: list, x: int, y: int):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if (0 <= ax < n) and 0 <= ay < n:
                if not isVisited2[ax][ay] and (
                    arr[x][y] == arr[ax][ay]
                    or (arr[x][y] == "R" and arr[ax][ay] == "G")
                    or (arr[x][y] == "G" and arr[ax][ay] == "R")
                ):
                    isVisited2[ax][ay] = True
                    queue.append((ax, ay))


n = int(input())

arr = []
isVisited1 = [[False for _ in range(n)] for _ in range(n)]
isVisited2 = [[False for _ in range(n)] for _ in range(n)]

for _ in range(n):
    arr.append(list(input().rstrip()))


answer1 = 0
answer2 = 0

for i in range(n):
    for j in range(n):
        if not isVisited1[i][j]:
            answer1 += 1
            isVisited1[i][j] = True
            dfs1(arr, i, j)
        if not isVisited2[i][j]:
            answer2 += 1
            isVisited2[i][j] = True
            dfs2(arr, i, j)


print(answer1, answer2)
