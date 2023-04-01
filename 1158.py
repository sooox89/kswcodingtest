#백준 1158번
from sys import stdin

n, k = map(int, stdin.readline().split())
queue = [i+1 for i in range(n)]
answer = []

while len(queue) !=0:
    for i in range(k-1):
        data = queue[0]
        queue.pop(0)
        queue.append(data)
    data = queue[0]
    queue.pop(0)
    answer.append(data)
print('<', end='')
print(*answer, sep = ', ' , end = '')
print('>')