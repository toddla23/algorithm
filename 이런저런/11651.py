N=int(input())
arr=[]
for i in range(N):
  a,b = map(int,input().split())
  arr.append((a,b))
arr = sorted(arr, key= lambda x: [x[1], x[0]])
for i in range(N):
    print(arr[i][0],arr[i][1])