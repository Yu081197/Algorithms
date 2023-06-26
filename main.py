import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
import heapq

n = int(input())
lectures = []


for i in range(n):
    id, start, end = map(int, input().split())
    heapq.heappush(lectures, (start, end))

heap = []
end = heapq.heappop(lectures)[1]
heapq.heappush(heap, end)
answer = 1

for i in range(n-1):
    new_start, new_end, heapq.heappop(lectures)
    end = heapq.heappop(heap)
    
