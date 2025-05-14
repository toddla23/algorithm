n = int(input())
arr = [-1, -1, 1,-1,1]

for i in range(5,n+1):
  a = arr[i-3]
  b = arr[i-5]
  if(a != -1 and b == -1):
    arr.append(a+1)
  elif (a == -1 and b != -1):
    arr.append(b+1)
  elif (a !=-1 and b != -1):
    arr.append(min(a,b) + 1)
  else:
    arr.append(-1)

    
    
  # print(f"i:{i} , arr: {arr}")
print(arr[n-1])