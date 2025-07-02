answers = set()

def calc(n: int, m: int, arr: list, numbers: list):
    global answers

    if len(arr) == m:
        answers.add(tuple(arr))
        return
    else:
        for i in range(len(arr), n):
            temp = arr.copy()
            temp.append(numbers[i])
            calc(n, m, temp, numbers)



n, m = map(int, input().split(" "))
numbers = list(map(int, input().split(" ")))
numbers.sort()
arr = []
calc(n, m, arr, numbers)

for ans in sorted(answers):
    print(" ".join(map(str, ans)))
