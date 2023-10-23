t = int(input())
if t == 1:
  print(t)
elif t == 2:
  print(3)
else:
  arr = [1] * (t+1)
  arr[1] = 1
  arr[2] = 3
  for i in range(3, t+1):
    arr[i] = arr[i-1] + (arr[i-2] * 2)
  print(arr[t]%10007)