def calc(n: int, m: int, arr: list, numbers: list):
    if len(arr) == m:
        print(" ".join(map(str, arr)))
        return
    else:
        for i in range(n):
            if(numbers[i] in arr):
                continue
            temp = arr.copy()
            temp.append(numbers[i])
            calc(n, m, temp, numbers)


n, m = map(int, input().split(" "))
numbers = list(map(int, input().split(" ")))
numbers.sort()
arr = []
calc(n, m, arr, numbers)
