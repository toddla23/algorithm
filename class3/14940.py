import sys
from collections import deque

input = sys.stdin.readline


def bfs(x: int, y: int, arr: list, zero:list) -> list:
    queue = deque()
    queue.append((x, y))
    answer_arr = [[-1 for i in range(m)] for i in range(n)]
    answer_arr[x][y] = 0
    # print(zero)
    for a, b in zero:
        # print(a, b)
        answer_arr[a][b] = 0

    while queue:
        x, y = queue.popleft()

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]


            if (0 <= tx < n) and 0 <= ty < m:
                if arr[tx][ty] == 1 and answer_arr[tx][ty] == -1:
                    answer_arr[tx][ty] = answer_arr[x][y] + 1
                    queue.append((tx, ty))
                # if arr[tx][ty] == 0:
                #     answer_arr[tx][ty] = 0
                # for i in answer_arr:
                #     print(i)
                    

    return answer_arr


n, m = map(int, input().split(" "))

arr = []

target_x = -1
target_y = -1
zero = []
for i in range(n):
    s = list(map(int, input().split(" ")))
    # if target_x == -1 and target_y == -1:
    for j in range(len(s)):
        if s[j] == 2:
            target_x = i
            target_y = j
        if s[j] == 0:
            zero.append((i,j))

    arr.append(s)

answer = bfs(target_x, target_y, arr, zero)

for i in answer:
    # print(list(map(str, i)))
    print(" ".join(list(map(str, i))))
