# 백준 2476번 주사위 게임
from sys import stdin
N = int(stdin.readline().strip()) ## int(input())
winning = 0
winner = 0
for i in range(N):
    a, b, c = map(int, stdin.readline().split())
    if a == b == c:
        winning = 10000 + a * 1000
    elif a == b or a == c:
        winning = 1000 + a * 100
    elif b == c:
        winning = 1000 + b * 100
    else:
        winning = max(a, b, c) * 100

    if winning > winner:
        winner = winning
print(winner)
