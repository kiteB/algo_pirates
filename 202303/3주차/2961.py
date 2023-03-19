# 도영이가 만든 맛있는 음식
from sys import stdin
from itertools import combinations

n = int(stdin.readline())
ingredients = list(range(n))
taste = [list(map(int, stdin.readline().split())) for _ in range(n)]
answer = 1e9

for i in range(1, n + 1):
    for combi in list(combinations(ingredients, i)):
        a = list(combi)
        s, b = 1, 0

        while a:
            idx = a.pop(0)
            s *= taste[idx][0]
            b += taste[idx][1]
        answer = min(answer, abs(s - b))

print(answer)
