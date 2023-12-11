import sys

def push(arr, num):
  arr.append(num)
  return arr

def pop(arr):
  if(len(arr) == 0):
    print(-1)
  else:
    print(arr[0])
  return arr[1:]

def size(arr):
  print(len(arr))
  return arr

def empty(arr):
  if(len(arr) == 0):
    print(1)
  else:
    print(0)
  return arr

def front(arr):
  if(len(arr) == 0):
    print(-1)
  else:
    print(arr[0])
  return arr

def back(arr):
  if(len(arr) == 0):
    print(-1)
  else:
    print(arr[-1])
  return arr

n = int(input())
arr = []
for i in range(n):
  commend = sys.stdin.readline().split()

  if(commend[0] == "push"):
    arr = push(arr, commend[1])
  elif(commend[0] == "pop"):
    arr = pop(arr)
  elif(commend[0] == "size"):
    arr = size(arr)
  elif(commend[0] == "empty"):
    arr = empty(arr)
  elif(commend[0] == "front"):
    arr = front(arr)
  elif(commend[0] == "back"):
    arr = back(arr)


