n = int(input())
arr = input().split(" ")

temp = [1 for i in range(n)]

for i in range(n, -1 , -1):
  for j in range(i,n):
    # print('i:',i,'j:',j)
    if(arr[i] > arr[j] and temp[i] <= temp[j]):
        temp[i] = temp[j]+1
  # print('i: ',i)
print(max(temp))
