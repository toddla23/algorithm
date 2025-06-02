import math

n = int(input())
arr = [0]
arr.append(1)

for i in range(2, n + 1):
    # print(f"i: {i}")
    temp = []

    x = int(math.sqrt(i))

    if x**2 == i:
        arr.append(1)
    else:
        a = 4
        for j in range(1, x + 1):
            result = arr[j**2] + arr[i - j**2]
            a = min(a, result)
            if result == 2:
                break

        arr.append(a)
#     print(f"temp: {temp}")
#     print(f"arr: {arr}")
# print(arr)
print(arr[-1])
