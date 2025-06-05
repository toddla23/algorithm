import sys
from collections import deque

visited = []


input = sys.stdin.readline
n, m = map(int, input().split(" "))
arr = []

x, y = 0, 0
answer = 0
visited = [[False] * m for _ in range(n)]
for i in range(n):
    input_arr = list(input().strip())
    arr.append(input_arr)
    if "I" in input_arr:
        x = input_arr.index("I")
        y = i

# visited[y][x] = True

to_visit = deque()
to_visit.append([x, y])

while to_visit:
    a, b = to_visit.popleft()
    if a < 0 or a >= len(arr[0]) or b < 0 or b >= len(arr):
        continue
    if visited[b][a] or arr[b][a] == "X":
        continue
    if arr[b][a] == "P":
        answer += 1
    visited[b][a] = True
    if a < len(arr[0]):
        to_visit.append([a + 1, b])
    if b < len(arr):
        to_visit.append([a, b + 1])
    if a - 1 >= 0:
        to_visit.append([a - 1, b])
    if b - 1 >= 0:
        to_visit.append([a, b - 1])
    # print(to_visit)


# print(arr)

# print(visited)
# print(len(visited))
print(answer if answer != 0 else "TT")
