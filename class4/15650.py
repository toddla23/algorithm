def calc(n: int, m: int, arr: list):
    if len(arr) == m:
        print(" ".join(map(str, arr[1:])))
        return

    elif len(arr) < m:
        for i in range(arr[-1] + 1, n + 1):
            temp = arr.copy()
            temp.append(i)
            calc(n, m, temp)


n, m = map(int, input().split(" "))
arr = [0]
calc(n, m + 1, arr)
