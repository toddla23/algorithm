arr = []

index = 0
for i in range(9):
  a = int(input())
  arr.append(a)
  if(max(arr) == a):
    index = i+1
  
print(max(arr))
print(index)