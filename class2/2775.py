for i in range(int(input())):
  k = int(input())
  n = int(input())
  
  arr = []
  arr.append([x for x in range(1, n+1)])
  for j in range(k):
    arr.append([sum(arr[j][:y+1]) for y in range(n)])
  print(arr[k])
  
  