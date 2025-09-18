import sys

input = sys.stdin.readline

dir = {}


def getFiboSize(k: int) -> int:

    if k == 1:
        dir[1] = 1
        return 1
    if k == 2:
        dir[2] = 1
        return 1

    result = (getFiboSize(k - 1) if k - 1 not in dir.keys() else dir[k - 1]) + (
        getFiboSize(k - 2) if k - 2 not in dir.keys() else dir[k - 2]
    )
    dir[k] = result

    return result


t = int(input())

for _ in range(t):
    k, p = list(map(int, input().split(" ")))

    result = getFiboSize(k)
    # print(result)
    # print(result[p])
    
    # print(f"result:{dir}")

    n = p+1
    temp = k
    while temp > 2:
        # print("_________________")
        # print(temp, n)
        if n <= dir[temp - 1]:
            temp = temp - 1
        else:
            n = n - dir[temp - 1]
            temp = temp - 2

    #     print(temp, n)
    #     print("_________________")
    # print(temp)
    print('a' if temp == 2 else 'b')