N=int(input())
arr=[]
for i in range(N):
  a,b = input().split(" ")
  arr.append([int(a),b])
arr = sorted(arr, key= lambda x: [x[0]])
# print(arr)
for i in range(N):
    print(arr[i][0],arr[i][1])