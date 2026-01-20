import copy


def clac(field, count, n):
    if count == n:
        return 1
    answer = 0
    for i in range(n):
        if not checkQueen(field, (count, i)):
            field[count][i] = True
            answer += clac(field, count + 1, n)
            field[count][i] = False
    return answer


def checkQueen(arr, queen):
    x, y = queen
    n = len(arr)

    # 열 검사
    for i in range(x):
        if arr[i][y]:
            return True

    # ↖ 대각선
    a, b = x - 1, y - 1
    while a >= 0 and b >= 0:
        if arr[a][b]:
            return True
        a -= 1
        b -= 1

    # ↗ 대각선
    a, b = x - 1, y + 1
    while a >= 0 and b < n:
        if arr[a][b]:
            return True
        a -= 1
        b += 1

    return False


n = int(input())
field = [[False] * n for _ in range(n)]

# for i in field:
#     print(i)


print(clac(field, 0, n))
