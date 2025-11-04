import sys

input = sys.stdin.readline


def LCS(s1, s2, m, n, arr):
    print(m, n)
    if m >= len(s1) or n >= len(s2):
        return
    if s1[m] == s2[n]:
        lastResult = ""
        if m - 1 >= 0 and n - 1 >= 0:
            lastResult = arr[m - 1][n - 1]
        arr[m][n] = lastResult + s1[m]
        return LCS(s1, s2, m + 1, n + 1, arr)

    elif s1[m] != s2[n]:
        lastResult1 = arr[m - 1][n] if m - 1 >= 0 else ""
        lastResult2 = arr[m][n - 1] if n - 1 >= 0 else ""
        if len(lastResult1) > len(lastResult2):
            arr[m][n] = lastResult1
        else:
            arr[m][n] = lastResult2
        LCS(s1, s2, m + 1, n, arr)
        LCS(s1, s2, m, n + 1, arr)


def lcs(s1, s2, arr):
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                lastResult = ""
                if i - 1 >= 0 and j - 1 >= 0:
                    lastResult = arr[i - 1][j - 1]
                arr[i][j] = lastResult + s1[i]
            else:
                lastResult1 = arr[i - 1][j] if i - 1 >= 0 else ""
                lastResult2 = arr[i][j - 1] if j - 1 >= 0 else ""
                if len(lastResult1) >= len(lastResult2):
                    arr[i][j] = lastResult1
                else:
                    arr[i][j] = lastResult2


n = int(input())
for _ in range(n):
    s1, s2 = input().rstrip().split(" ")
    # print(s1)
    # print(s2)
    arr = [["" for _ in range(len(s2))] for _ in range(len(s1))]

    result = lcs(s1, s2, arr)
    print(len(arr[-1][-1]), arr[-1][-1])
    # for i in arr: 
    #     print(i)
