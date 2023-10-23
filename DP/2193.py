t = int(input())

arr = [[0 for i in range(2)] for j in range(t)]
arr[0] = [0, 1]

for i in range(1,t):
  arr[i][0] = arr[i-1][1] + arr[i-1][0]
  arr[i][1] = arr[i-1][0]

print(sum(arr[t-1]))