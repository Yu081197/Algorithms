import sys
import copy

input = sys.stdin.readline

# 완전탐색
def recursive(arr, n):
    if len(arr) == n:
        operators_list.append(copy.deepcopy(arr))
        return
    arr.append(" ")
    recursive(arr, n)
    arr.pop()
    arr.append('+')
    recursive(arr, n)
    arr.pop()
    arr.append('-')
    recursive(arr, n)
    arr.pop()

t = int(input())

for _ in range(t):
    operators_list = []
    n = int(input())
    recursive([], n -1 )
    integers = [i for i in range(1, n + 1)]

    for operators in operators_list:
        string = ""
        for i in range(n - 1):
            string += str(integers[i]) + operators[i]
        string += str(integers[-1])
        if eval(string.replace(" ", "")) == 0:
            print(string)
    print()
