t = int(input())

arr = [[0 for j in range(10)] for i in range(t)]
arr[0] = [0,1,1,1,1,1,1,1,1,1]

for i in range(1, t):
  arr[i][0] = arr[i-1][1]
  for j in range(1,9):
    arr[i][j] = arr[i-1][j-1] + arr[i-1][j+1]
    # print("i:", i , "j:" , j , "result = ", arr[i][j])
  arr[i][9] = arr[i-1][8]

print(sum(arr[t-1])%1000000000)