import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(startX, startY, map, isVisit, r, c):
    count = 1
    toVisit = deque([(startX, startY)])
    isVisit[startX][startY] = True

    while toVisit:
        x, y = toVisit.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if (0 <= tx < r and 0 <= ty < c) and not isVisit[tx][ty] and map[tx][ty] == '#':
                toVisit.append((tx, ty))
                isVisit[tx][ty] = True
                count+=1
    # print(count)
    return count

t = int(input())
for _ in range(t):
    r, c = list(map(int, input().split()))

    isVisit = [[False for _ in range(c)] for _ in range(r)]

    arr = []
    for _ in range(r):
        tmep = input().rstrip()
        arr.append(tmep)


    # print(arr)
    # print(arr[0][0])
    answer = 0
    for i in range(r):
        for j in range(c):
            if not isVisit[i][j] and arr[i][j] == '#':
                answer = max(dfs(i,j,arr,isVisit,r,c), answer)
                
    print(answer)
