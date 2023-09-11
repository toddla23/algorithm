t = int(input())
if(t == 1):
  print(1)
elif(t == 2):
  print(2)
else:
  arr = [1] * (t+1)
  arr[2] = 2

  for i in range(3, t+1):
    # print(i)
    arr[i] = arr[i-1] + arr[i-2]
    # print(arr)

  print(arr[t]%10007)