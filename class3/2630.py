white = 0
blue = 0


def check(arr: list, x: int, y: int, length: int):
    # print(f"x: {x}, y: {y}, length: {length}")
    a = 0
    for i in range(length):
        a += sum(arr[y + i][x : x + length])

    if a == 0:
        global white
        white = white + 1
        # print("true")
        # for i in range(length):
        #     print(arr[y + i][x : x + length])
    elif a == length**2:
        global blue
        blue = blue + 1
        # print("true")
        # for i in range(length):
        #     print(arr[y + i][x : x + length])
    else:
        # print("false")
        check(arr=arr, x=x, y=y, length=length // 2)
        check(arr=arr, x=x + length // 2, y=y, length=length // 2)
        check(arr=arr, x=x, y=y + length // 2, length=length // 2)
        check(arr=arr, x=x + length // 2, y=y + length // 2, length=length // 2)


n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split(" "))))
# print(arr)

check(arr=arr, x=0, y=0, length=n)
print(white)
print(blue)
