n = int(input())
answer = 0
# 1 , 6 = 7, 6+6 = 19, 6+6+6 = 37
arr = [1]
while n> max(arr):
  # print(arr)
  answer = answer + 1
  arr.append(max(arr) + 6 * answer)
  
print(answer+1)