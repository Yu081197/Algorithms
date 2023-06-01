from collections import deque
import sys
sys.stdin = open("input.txt", "r")

tc = int(input())
for _ in range(tc):
    data = input()
    left_stack = []
    right_stack = []
    for i in data:
        if i == '-':
            if left_stack:
                left_stack.pop()
        elif i == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif i == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        else:
            left_stack.append(i)
            
    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))