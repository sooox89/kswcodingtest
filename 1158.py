#백준 1158번
from sys import stdin

n, k = map(int, stdin.readline().split())
queue = [i+1 for i in range(n)]
answer = []
front = 0
rear = 0

while len(queue) !=0:
    data = queue[(front+k-1)%len(queue)]
    front = (front + k-1) % len(queue)
    queue.pop(front)
    answer.append(data)
print('<', end='')
print(*answer, sep = ', ' , end = '')
print('>')