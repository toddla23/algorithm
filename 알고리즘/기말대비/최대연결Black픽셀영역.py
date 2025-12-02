import sys
from collections import deque

input = sys.stdin.readline


def bfs(sr, sc, grid, visited):
    q = deque([(sr, sc)])
    visited[sr][sc] = True
    cnt = 1

    while q:
        r, c = q.popleft()

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m:
                if not visited[nr][nc] and grid[nr][nc] == "#":
                    visited[nr][nc] = True
                    cnt += 1
                    q.append((nr, nc))
    return cnt


t = int(input())

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for _ in range(t):
    n, m = map(int, input().split())
    grid = [list(input().strip()) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    max_area = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == "#" and not visited[i][j]:
                max_area = max(max_area, bfs(i, j, grid, visited))

    print(max_area)
    for i in grid:
        print(i)
    for i in visited:
        print(i)