def calc(n: int, m: int, arr: list):
    if len(arr) == m:
        print(" ".join(map(str, arr[1:])))
        return
    else:
        for i in range(arr[-1] if arr[-1] != 0 else 1, n):
            temp = arr.copy()
            temp.append(i)
            calc(n, m, temp)


n, m = map(int, input().split(" "))
arr = [0]
calc(n + 1, m + 1, arr)
