[a, b] = list(map(int, input().split(" ")))

top  = a + 1 + b - 1 - 1
b = b - 1
bottom = 1
tempTop = 1
for i in range(b):
  # print("top : ", top - i , "bottom: ", b - i)
  tempTop = tempTop * (top - i)
  bottom = bottom * (b - i)

# print(tempTop)
# print(bottom)
print(int(tempTop/bottom)%1000000000)
