from collections import deque
import sys



sys.stdin = open("input.txt", "r")

k = int(input())
stack = []

for _ in range(k):
    x = int(input())
    if x == 0:
        stack.pop()
    else :
        stack.append(x)
        
print(sum(stack))