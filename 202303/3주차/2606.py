# 바이러스
import sys
sys.setrecursionlimit(10**9)


def dfs(start):
    global cnt
    visited[start] = 1

    for node in graph[start]:
        if not visited[node]:
            cnt += 1
            dfs(node)


computer = int(sys.stdin.readline())
graph = [[] for _ in range(computer + 1)]
visited = [False] * (computer + 1)

for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
dfs(1)
print(cnt)
