t = int(input())

arr = [0 for i in range(100)]
arr[0] = 1
arr[1] = 1
arr[2] = 1
arr[3] = 2
arr[4] = 2

for i in range(5, 100):
  arr[i] = arr[i-1] + arr[i-5]

for i in range(t):
  a = int(input())
  print(arr[a-1])
