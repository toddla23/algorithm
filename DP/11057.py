t = int(input())

arr = [[0 for i in range(10)] for j in range(t)]
arr[0] = [1,1,1,1,1,1,1,1,1,1]

for i in range(1,t):
  arr[i][0] = 1
  for j in range(1,10):
    arr[i][j] = sum(arr[i-1][0:j+1])

# print(arr)
print(sum(arr[t-1]) %  10007)