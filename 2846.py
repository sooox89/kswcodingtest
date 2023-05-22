# 오르막길
from sys import stdin
n = int(input())
height = list(map(int,stdin.readline().split()))
start = height[0]
cal = 0
answer = []

for i in range(1,n):
    if height[i] > start:
        cal += height[i] - start
        start = height[i]

    elif height[i] == start or height[i] < start :
        answer.append(cal)
        start = height[i]
        cal = 0

answer.append(cal)
print(max(answer))

