import sys

input = sys.stdin.readline


def lcs(s1, s2, m, n, arr):
    # print(m, n)
    result = 0
    # print(f"m: {m}, n: {n}")

    if m == -1 or n == -1:
        return 0

    elif m > -1 and n > -1 and s1[m] == s2[n]:
        if m == 0 or n == 0:
            arr[m][n] = 1
        elif arr[m - 1][n - 1] != -1:
            arr[m][n] = arr[m - 1][n - 1] + 1
        else:
            arr[m][n] = lcs(s1, s2, m - 1, n - 1, arr) + 1
        return arr[m][n]

    elif m > -1 and n > -1 and s1[m] != s2[n]:
        r1 = arr[m - 1][n] if m != 0 else 0
        r2 = arr[m][n - 1] if n != 0 else 0
        if r1 == -1:
            r1 = lcs(s1, s2, m - 1, n, arr)
        if r2 == -1:
            r2 = lcs(s1, s2, m, n - 1, arr)
        arr[m][n] = max(r1, r2)
        return arr[m][n]


n = int(input())

for _ in range(n):
    s1, s2 = input().rstrip().split(" ")
    # s1 = "abcbdab"
    # s2 = "bdcaba"
    # print(s1)
    # print(s2)
    # print(len(s1), len(s2))
    arr = [[-1 for _ in range(len(s2))] for _ in range(len(s1))]
    result = lcs(s1, s2, len(s1) - 1, len(s2) - 1, arr)
    # for i in arr:
    #     print(i)
    print(result)
