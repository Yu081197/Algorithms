from collections import deque
import sys
input = sys.stdin.readline
n, w, l = map(int, input().split())
arr = list(map(int, input().split()))
arr.reverse()

q = deque()
total = 0
t = 0

while True:
    if len(arr) == 0 and total == 0:
        break
    if len(q) == w:
        x = q.popleft()
        total -= x
    if len(arr) > 0 and total + arr[-1] <= l:
        q.append(arr[-1])
        total += arr[-1]
        arr.pop()
    else:
        q.append(0)
    t += 1
    
print(t)