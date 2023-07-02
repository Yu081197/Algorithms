import sys

input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))


arr = sorted(arr)
for data in arr:
    print(data)
