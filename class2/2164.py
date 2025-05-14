def pop(arr:list):
  return arr[1:]

n = int(input())

arr = list(range(1,n+1))
while len(arr) != 1:
  if(len(arr)%2 == 0):
    arr = arr[1::2]
  else:
    temp = [arr[-1]]
    temp.extend(arr[1::2])
    arr = temp[:]
  # print(arr)
  
print(arr[0])