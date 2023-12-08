a = int(input())
arr = []

for i in range(a):
  arr.append(int(input()))
  for j in range(i, 0, -1):
    if arr[j] < arr[j-1]:
      temp = arr[j]
      arr[j] = arr[j-1]
      arr[j-1] = temp

for i in arr:
  print(i)