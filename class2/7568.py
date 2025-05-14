arr = []
for i in range(int(input())):
  arr.append(list(map(int,input().split(" "))))

origin = arr[:]

arr.sort(key=lambda x : x[0])
arr.reverse()

print(arr)

rank = [1]
for i in range(1, len(arr)):
    if(arr[i-1][0] > arr[i][0]):
      if(arr[i-1][1] >= arr[i][1]):
        rank.append(i+1)
      else:
        rank.append(rank[i-1])
    if(arr[i-1][0] == arr[i][0]):
      if(arr[i-1][1] > arr[i][1]):
        rank.append(i+1)
      elif(arr[i-1][0] == arr[i][0]):
        rank.append(rank[i-1])
      
        
    print(rank)

      


print(" ".join([str(rank[arr.index(i)]) for i in origin]))