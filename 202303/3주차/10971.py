# 외판원 순회 2
from sys import stdin


def dfs(start, now, cost):
    global graph, visited, min_cost

    if (now == start) and (visited.count(False) == 0):
        min_cost = min(min_cost, cost)

    for i in range(n):
        if not graph[now][i] == 0 and not visited[i]:
            visited[i] = True
            dfs(start, i, cost + graph[now][i])
            visited[i] = False


n = int(stdin.readline())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]

min_cost = 1e9
visited = [False for _ in range(n)]
dfs(0, 0, 0)

print(min_cost)
