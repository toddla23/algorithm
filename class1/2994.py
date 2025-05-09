import datetime

h, m = map(int, input().split(" "))

time = datetime.datetime(2000, 1, 1, hour=h, minute=m)

result = time - datetime.timedelta(minutes=45)

print(f"{result.hour} {result.minute}")