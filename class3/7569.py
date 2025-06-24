import sys

input = sys.stdin.readline


def bfs(arr: list, toVisit: list):
    global visited
    global visitCount
    willVisit = []
    for i in toVisit:
        x, y, z = i
        dx = [1, -1, 0, 0, 0, 0]
        dy = [0, 0, 1, -1, 0, 0]
        dz = [0, 0, 0, 0, 1, -1]
        for i in range(6):
            ax = x + dx[i]
            ay = y + dy[i]
            az = z + dz[i]
            if 0 <= ax < h and 0 <= ay < m and 0 <= az < n:
                if visited[ax][ay][az] == False and arr[ax][ay][az] != -1:
                    visited[ax][ay][az] = True
                    willVisit.append((ax, ay, az))
                    visitCount += 1 
    return willVisit


n, m, h = map(int, input().split(" "))

arr = []
toVisit = []
total = 0
visitCount = 0

visited = [[[False for _ in range(n)] for _ in range(m)] for _ in range(h)]

for i in range(h):
    temp = []
    for j in range(m):
        t = list(map(int, input().split(" ")))
        for k in range(n):
            if t[k] == 1:
                visited[i][j][k] = True
                toVisit.append((i, j, k))
            if t[k] == 0:
                total += 1

        temp.append(t)
    arr.append(temp)

# print(arr)
# print(toVisit)
# print(visited)
answer = 0

while toVisit:
    toVisit = bfs(arr=arr, toVisit=toVisit)
    answer += 1
    # print(toVisit)
    # for i in visited:
    #     for j in i:
    #         print(j)
    #     print("_________________________________")


if(total!=  visitCount):
    print(-1)
else:
    print(answer - 1)
