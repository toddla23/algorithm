t = int(input())
for _ in range(t):
    a, b = input().split()

    na = len(a) + 1
    nb = len(b) + 1

    arr = [[""] * nb for _ in range(na)]

    for i in range(na):
        for j in range(nb):
            if i == 0 or j == 0:
                arr[i][j] = ""
                continue

            elif a[i-1] == b[j-1]:
                arr[i][j] = arr[i - 1][j - 1] + a[i-1]
            else:
                arr[i][j] = arr[i-1][j] if len(arr[i - 1][j]) > len(arr[i][j - 1]) else arr[i][j-1]
        
    print(len(arr[-1][-1]), arr[-1][-1])