import sys

input = sys.stdin.readline


def dfs(x, y, arr, logs):
    if arr[x][y] in logs:
        return 0

    logs = logs + arr[x][y]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    answer = 1

    for i in range(4):
        ax = x + dx[i]
        ay = y + dy[i]
        if 0 <= ax < r and 0 <= ay < c:
            answer = max(dfs(ax, ay, arr, logs) + 1, answer)
    return answer


r, c = list(map(int, input().split()))

arr = []
for _ in range(r):
    temp = list(input().rstrip())
    arr.append(temp)


# print(arr)
answer = dfs(0, 0, arr, "")
print(answer)
