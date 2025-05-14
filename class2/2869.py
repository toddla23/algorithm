import math
a,b,v = map(int, input().split(" "))

# l = 0
# answer = 0
# while True:
#   answer = answer+1
#   l = l+a
#   if(l < v):
#     l = l-b
#   else:
#     break
  
# # 하루동안 올라가는 길이가 a-b 니까
    
print(math.ceil((v-a)/(a-b))+1)