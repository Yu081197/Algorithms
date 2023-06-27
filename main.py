import sys
from collections import deque


sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

s1, s2, s3 = map(int, input().split())
result = []

for i in range(1, s1 + 1):
    for j in range(1, s2 + 1):
        for k in range(1, s3 + 1):
            summary = i + j + k
            result.append(summary)
result.sort()


s = list(set(result))
cnt = []
for i in s:
    cnt.append(result.count(i))
print(s[cnt.index(max(cnt))])
