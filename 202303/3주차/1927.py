# 최소 힙
from sys import stdin
import heapq

n = int(stdin.readline())
heap = []

for _ in range(n):
    x = int(stdin.readline())

    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heap[0])
            heapq.heappop(heap)
    else:
        heapq.heappush(heap, x)
