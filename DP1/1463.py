a = int(input())

arr = [0]

for i in range(1, a+1):
  if(i == 1):
    arr.append(0)
  else:
    arr.append(min(arr[i-1] + 1, arr[i // 2] + 1 if i%2 == 0 else arr[i-1] + 1, arr[i // 3] + 1 if i%3 == 0 else arr[i-1] + 1))
print(arr[i])