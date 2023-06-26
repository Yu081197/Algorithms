import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline



n = int(input())
lectures = []


for i in range(n):
    id, start, end = map(int, input().split())
