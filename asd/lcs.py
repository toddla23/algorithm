s1 = "AGGTAB"
s2 = "GXTXAYB"


def calc(s1, s2):

    arr = [["" for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                arr[i][j] = arr[i - 1][j - 1] + s1[i - 1]
                continue
            arr[i][j] = (
                arr[i - 1][j]
                if len(arr[i - 1][j]) > len(arr[i][j - 1])
                else arr[i][j - 1]
            )

    for i in arr:
        print(i)


calc(s1, s2)
