import sys
input = sys.stdin.readline
from collections import deque
import heapq


heap = []
n = int(input())
for i in range(n):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            absolute, original = heapq.heappop(heap)
            print(original)
    else:
        heapq.heappush(heap, (abs(x), x))