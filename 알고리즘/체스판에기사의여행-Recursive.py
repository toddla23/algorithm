import sys

input = sys.stdin.readline
answer = []
found = False


def calc(s, a, b, arr, count):
    global answer
    global found

    # saywoo1021@kookmin.ac.kr

    if found:
        return s

    arr[a][b] = count

    # print(count)
    # for i in arr:
    #         print(i)

    if count == s:
        # print(count)
        answer = [temp[:] for temp in arr]
        found = True
        # for i in answer:
        #     print(i)

        return count

    x = [-2, -1, 1, 2, 2, 1, -1, -2]
    y = [1, 2, 2, 1, -1, -2, -2, -1]
    # if arr[a][b] != 0:
    #     return

    result = 0
    for i in range(8):
        p = a + x[i]
        q = b + y[i]
        if (0 <= p < m and 0 <= q < n) and (arr[p][q] == 0):
            result = calc(s, p, q, arr, count + 1)
            if found:
                break
        # if 0 <= p < m and 0 <= q < n:
        #     result = calc(s, p, q, arr, count + 1)

    arr[a][b] = 0

    return result


t = int(input())

for _ in range(t):
    m, n, a, b = list(map(int, input().split(" ")))
    arr = [[0 for _ in range(n)] for _ in range(m)]
    answer = [[0 for _ in range(n)] for _ in range(m)]
    found = False
    calc(m * n, a - 1, b - 1, arr, 1)

    # for i in arr:
    #     print(" ".join(map(str, i)))

    # for i in answer:
    #     print(" ".join(map(str, i)))

    if answer[0][0] + answer[0][1] > 1:
        print(1)
        for i in answer:
            print(" ".join(map(str, i)))
    else:
        print(0)
