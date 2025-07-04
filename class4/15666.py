answers = set()

def calc(start:int, arr: list):
    if len(arr) == m:
        print(" ".join(map(str, arr)))
        return
    else:
        for i in range(start, len(numbers)):
            temp = arr.copy()
            temp.append(numbers[i])
            calc(i, temp)



n, m = map(int, input().split(" "))
numbers = list(map(int, input().split(" ")))
numbers = sorted(set(numbers))
calc(0,[])


