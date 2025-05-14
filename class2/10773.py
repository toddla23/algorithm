arr = []
for i in range(int(input())):
  n = int(input())
  if(n == 0):
    arr.pop()
  else:
    arr.append(n)
    
print(sum(arr))