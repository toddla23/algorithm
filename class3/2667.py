import sys
from collections import deque

input = sys.stdin.readline


def bfs(x: int, y: int, arr: list):
    global visited
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    count = 1
    while queue:
        x, y = queue.popleft()
        # print(x, y)
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if (0 <= a < n) and (0 <= b < n):
                if not visited[a][b]:
                    if arr[a][b] == "1":
                        count += 1
                        visited[a][b] = True
                        queue.append((a, b))

    return count


n = int(input())
arr = []

for _ in range(n):
    arr.append(list(input().rstrip()))

visited = [[False for _ in range(n)] for _ in range(n)]


answer_arr = []
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == "1":
            if not visited[i][j]:

                answer_arr.append(bfs(i, j, arr))
                # print(answer_arr)

print(len(answer_arr))
answer_arr.sort()

for ans in answer_arr:
    print(ans)
