import sys

input = sys.stdin.readline

m, n = map(int, input().split(" "))

arr = []
toVisit = []
isVisit = [[False for _ in range(m)] for _ in range(n)]
total = 0

for i in range(n):
    s = list(map(int, input().rstrip().split(" ")))
    arr.append(s)
    for j in range(m):
        if s[j] == 1:
            isVisit[i][j] = True
            toVisit.append((i, j))
        if s[j] == 0:
            total += 1

answer = 0
count = 0
while toVisit:
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    temp = []
    for i in toVisit:
        x, y = i
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]

            if (0 <= ax < n) and 0 <= ay < m:
                if (isVisit[ax][ay] == False) and arr[ax][ay] == 0:
                    isVisit[ax][ay] = True
                    count += 1
                    temp.append((ax, ay))
    toVisit = temp
    answer += 1

print(answer-1 if total == count else -1)
