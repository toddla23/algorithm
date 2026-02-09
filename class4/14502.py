import sys
from collections import deque
import copy
from itertools import combinations

input = sys.stdin.readline


def bfs(arr, n, m):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = deque()
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if (0 <= ax and ax < n) and (0 <= ay and ay < m):
                if arr[ax][ay] == 0:
                    arr[ax][ay] = 2
                    queue.append((ax, ay))

    answer = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                answer += 1

    # for i in arr:
    #     print(i)

    return answer


arr = []

n, m = list(map(int, input().split()))

for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)

# for i in arr:
#     print(i)for i in arr:
#     print(i)


coords = [(i, j) for i in range(n) for j in range(m)]
answer = 0
for (x1, y1), (x2, y2), (x3, y3) in combinations(coords, 3):
    temp_arr = copy.deepcopy(arr)
    if temp_arr[x1][y1] + temp_arr[x2][y2] + temp_arr[x3][y3] != 0:
        continue
    temp_arr[x1][y1] = 1
    temp_arr[x2][y2] = 1
    temp_arr[x3][y3] = 1
    answer = max(bfs(temp_arr, n, m), answer)

print(answer)

