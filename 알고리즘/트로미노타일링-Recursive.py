import sys

input = sys.stdin.readline
count = 1

def asd(arr):
    for i in arr:
        print(" ".join(map(str,i)))


def check(arr, x_start, x_end, y_start, y_end):
    for i in range(x_start, x_end + 1):
        for j in range(y_start, y_end + 1):
            if arr[i][j] != 0:
                return False
    return True


def calc(arr, x_start, x_end, y_start, y_end):
    global count
    # print(x_start, x_end, y_start,y_end)
    if x_start == x_end or y_start == y_end:
        return
    dt = [
        (x_start, (x_start + x_end) // 2, y_start, (y_start + y_end) // 2),
        (x_start, (x_start + x_end) // 2, (y_start + y_end) // 2 + 1, y_end),
        ((x_start + x_end) // 2 + 1, x_end, y_start, (y_start + y_end) // 2),
        ((x_start + x_end) // 2 + 1, x_end, (y_start + y_end) // 2 + 1, y_end),
    ]
    checkResult = []
    for i, j, k, l in dt:
        checkResult.append(check(arr, i, j, k, l))
        
    xmid = (x_start + x_end) // 2
    ymid = (y_start + y_end) // 2
    target = [(xmid, ymid), (xmid, ymid + 1), (xmid + 1, ymid), (xmid + 1, ymid + 1)]
    
    for i in range(4):
        if checkResult[i]:
            x, y = target[i]
            arr[x][y] = count
    count += 1
            
    for i, j, k, l in dt:
        calc(arr, i, j, k, l)

    return


t = int(input())


for _ in range(t):
    n = int(input())
    i, j = list(map(int, input().split(" ")))
    arr = [[0 for _ in range(n)] for _ in range(n)]
    arr[i][j] = -1
    count = 1
    calc(arr, 0, n - 1, 0, n - 1)
    arr[i][j] = 0

    asd(arr)
