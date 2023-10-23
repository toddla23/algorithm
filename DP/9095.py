n = int(input())

arr = [1] * (11+1)
arr[2] = 2
arr[3] = 4

for i in range(4, 11 + 1):
  arr[i] = arr[i-3]+ arr[i-1] + arr[i-2]

for i in range(n):
  t = int(input())
  print(arr[t])