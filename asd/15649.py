def calc(arr, n, s):
    # print(f"s: {s}, arr: {arr}")
    if len(s) == n:
        print(" ".join(s))
        return

    for i in range(len(arr)):
        calc(arr[:i] + arr[i + 1 :], n, s +[arr[i]])


n, m = list(map(int, input().split()))

arr = [str(i) for i in range(1, n + 1)]

calc(arr, m, [])
