n = int(input())
arr = [1] * (n + 1)


for i in range(1, n + 1):
    arr[i] = (2 * arr[i - 1] + arr[i - 2]) % 9901

print(arr[n])
