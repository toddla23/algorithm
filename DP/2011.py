a = input()

arr = [1]
x = 0
for i in range(1, len(a)):
  if(a[i] == '0' and int(a[i-1]) >= 2):
    x = 1
    break

  if(int(a[i-1:i+1]) > 9 and int(a[i-1:i+1]) < 27):
    arr.append(arr[i-2]+ arr[i-1])
  else:
    arr.append(arr[i-1])

print(arr)

if(a[0] == '0' or x == 1):
  print(0)
else:
  print(arr[-1]%1000000)
