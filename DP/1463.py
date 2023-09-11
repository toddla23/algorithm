t = int(input())
arr = [1] * (t + 1)
arr[1] = 0


for i in range(4, t+1):
  # print(i)
  temp = [t+1]*3
  if i % 3 == 0:
    temp[0] = arr[i//3] + 1
  if i % 2 == 0:
    temp[1] = arr[i//2] + 1
  temp[2] = arr[i-1] + 1
  # print(temp)
  arr[i] = min(temp)
  # print(arr)

print(arr[t])