n = int(input())
arr = list(map(int,input().split(" ")))

sosu = []
for i in range(2, max(arr) + 1):
  temp = 0
  for j in sosu:
    if( i % j == 0):
      # print(i)
      temp = 1
      break
  # print(i, temp)
  if(temp == 0):
    sosu.append(i)
  
answer = 0
for i in arr:
  if sosu.count(i):
    answer = answer + 1
    
# print(sosu)
print(answer)