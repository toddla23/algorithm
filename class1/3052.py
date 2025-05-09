arr=  []
for i in range(10):
  arr.append(int(input())%42)

x = list(set(arr))
print(len(x))
