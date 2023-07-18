from collections import deque
import sys

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

MAX = 100001
n, k = map(int, input().split())
arr = [0] * MAX


def bfs():
    q = deque([n])
    while n:
        x = q.popleft()
        if x == k:
            return arr[x]
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx < MAX and not arr[nx]:
                arr[nx] = arr[x] + 1
                q.append(nx)


print(bfs())
