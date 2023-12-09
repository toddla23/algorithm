N=int(input())
arr=[]
for i in range(N):
  a, b, c, d = input().split(" ")
  arr.append([a,int(b), int(c), int(d)])
arr = sorted(arr, key= lambda x: [-int(x[1]), int(x[2]), -int(x[3]), x[0]])
# print(arr)
for i in range(N):
    print(arr[i][0])

