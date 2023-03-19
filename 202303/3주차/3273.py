# 두 수의 합
from sys import stdin

n = int(stdin.readline())
numbers = sorted(list(map(int, stdin.readline().split())))
x = int(stdin.readline())

start = 0
end = n - 1
cnt = 0

while start < end:
    total = numbers[start] + numbers[end]

    if total == x:
        cnt += 1
        start += 1
        end -= 1
    elif total < x:
        start += 1
    else:
        end -= 1

print(cnt)
