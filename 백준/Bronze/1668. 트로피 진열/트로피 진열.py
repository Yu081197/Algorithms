import sys
input = sys.stdin.readline

def trophy(h):
    max = -1
    count = 0
    for i in h:
        if max < i:
            max = i
            count += 1
    return count

n = int(input())
h = []

for i in range(n):
    h.append(int(input()))

print(trophy(h))
print(trophy(reversed(h)))