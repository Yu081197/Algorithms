import sys
input = sys.stdin.readline
from collections import deque

result = 0
max_value = 0

for i in range(5):
    row = list(map(int, input().split()))
    summury = sum(row)
    if max_value < summury:
        max_value = summury
        result = i + 1
        
print(result, max_value)