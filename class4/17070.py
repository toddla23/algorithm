from collections import deque


def bfs(status: int, x: int, y: int, arr, n, answer):  # status 1:가로 2: 세로 3: 대각선

    tovisits = deque()
    tovisits.append((status, x, y))
    while tovisits:
        status, x, y = tovisits.popleft()
        answer[x][y] += 1

        if status == 1:  # 현재상태 가로
            if y + 1 < n and arr[x][y + 1] != 1:  # 가로
                tovisits.append((1, x, y + 1))

            if (
                x + 1 < n
                and y + 1 < n
                and arr[x][y + 1] != 1
                and arr[x + 1][y] != 1
                and arr[x + 1][y + 1] != 1
            ):  # 대각
                tovisits.append((3, x + 1, y + 1))

        if status == 2:  # 현재상태 세로
            if x + 1 < n and arr[x + 1][y] != 1:  # 세로
                tovisits.append((2, x + 1, y))

            if (
                x + 1 < n
                and y + 1 < n
                and arr[x][y + 1] != 1
                and arr[x + 1][y] != 1
                and arr[x + 1][y + 1] != 1
            ):  # 대각
                tovisits.append((3, x + 1, y + 1))

        if status == 3:  # 현재상태 대각
            if y + 1 < n and arr[x][y + 1] != 1:  # 가로
                tovisits.append((1, x, y + 1))
            if x + 1 < n and arr[x + 1][y] != 1:  # 세로
                tovisits.append((2, x + 1, y))

            if (
                x + 1 < n
                and y + 1 < n
                and arr[x][y + 1] != 1
                and arr[x + 1][y] != 1
                and arr[x + 1][y + 1] != 1
            ):  # 대각
                tovisits.append((3, x + 1, y + 1))

    return 0


n = int(input())
arr = []
for _ in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)
answer = [[0] * n for _ in range(n)]

bfs(1, 0, 1, arr, n, answer)

# for i in answer:
#     print(i)
print(answer[-1][-1])
