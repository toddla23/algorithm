a, b = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

answer = []
for i in range(len(arr)):
  for j in range(i+1, len(arr)):
    for k in range(j+1, len(arr)):
      # print(arr[i] , arr[j] , arr[k], arr[i] + arr[j] + arr[k])
      if(arr[i] + arr[j] + arr[k] <= b):
        # answer.append([arr[i] , arr[j] , arr[k]])
        # print(arr[i] + arr[j] + arr[k])
        answer.append([arr[i] + arr[j] + arr[k]])

a = max(answer)
        
# print(int(max(answer)))
# print(answer)
print(a[0])