# 평범한 배낭
from sys import stdin

n, k = map(int, stdin.readline().split())
items = [[0, 0]] * (n + 1)

for i in range(1, n + 1):
    w, v = map(int, stdin.readline().split())
    items[i] = [w, v]

# dp[i][j] : 물건을 [1 ~ i]까지 고려하고 배낭의 용량이 [j]일 때, 얻을 수 있는 최대 가치
dp = [[0] * (k + 1) for _ in range(n + 1)]

for idx in range(1, n + 1):
    weight = items[idx][0]
    value = items[idx][1]

    for bag_weight in range(1, k + 1):
        if weight > bag_weight:  # 물건의 무게가 배낭의 용량보다 클 때
            dp[idx][bag_weight] = dp[idx - 1][bag_weight]
        else:  # 최댓값 갱신
            dp[idx][bag_weight] = max(dp[idx - 1][bag_weight], dp[idx - 1][bag_weight - weight] + value)

print(dp[n][k])
