import sys

input = sys.stdin.readline


def calc(n, log,arr):
    answer = []
    temp = []
    for j in range(n):
        minlength = float("inf")
        minIndex = 0
        for i in range(len(log) - 1):
            logLength = log[i] + log[i + 1]
            if minlength > logLength:
                minlength = logLength
                minIndex = i
        log[minIndex + 1] = log[minIndex] + log[minIndex + 1]
        temp.append(arr[minIndex])
        arr.pop(minIndex)
        log.pop(minIndex)   
        answer.append(minlength)
        # print(j)
        # print(f"temp: {temp}")
        # print(f"log: {log}")
        # print(f"answerList: {answer}")
        # print(f"answer: {sum(answer)}")
        
        

    return sum(answer)


n = int(input())
for _ in range(n):
    l, t = list(map(int, input().split(" ")))
    arr = list(map(int, input().split(" ")))
    log = [arr[0]]
    for i in range(t - 1):
        log.append(arr[i + 1] - arr[i])

    log.append(l - arr[-1])
    print(log)
    calc(len(log)-1, log, arr)
