import sys

sys.setrecursionlimit(1000)  # 예시: 재귀 깊이 제한을 높임

input = sys.stdin.readline


def matrixMult(arr1, arr2):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            temp = 0
            for k in range(2):
                temp += arr1[i][k] * arr2[k][j]
            result[i][j] = temp %1000

    return result


def fibo3(n: int):
    arr = [[1, 1], [1, 0]]
    if n == 1:
        return [temp[:] for temp in arr]
    # print(n)
    if n % 2 == 0:
        temp = fibo3(n//2)
        return matrixMult(temp,temp)
    else:
        return matrixMult(fibo3(n - 1), arr)


t = int(input())

for _ in range(t):
    n = int(input())
    result = fibo3(n+1)
    print(result[1][1])
