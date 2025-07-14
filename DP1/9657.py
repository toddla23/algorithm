n = int(input())
turn = 0
arr = [False for _ in range(n+2)]
arr[2] = True
for i in range(5, n + 1):
    if(not arr[i-1] and not arr[i-3] and not arr[i-4]):
        arr[i] = True
    
    # print(arr)
    
print("SK" if not arr[n] else"CY" )
