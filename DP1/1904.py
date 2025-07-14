n = int(input())
arr = [0 for _ in range(n + 2)]
arr[0] = 1
arr[1] = 2

for i in range(2, n):
    arr[i] = (arr[i-1] + arr[i-2])%15746
    
print(arr[n-1]%15746)
