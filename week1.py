# 백준 2965번
from sys import stdin
a, b, c = map(int, stdin.readline().split())
n = 0
if b-a >= c-b:
    n = b-a-1
elif b-a < c-b:
    n = c-b-1
print(n)