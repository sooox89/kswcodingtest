#백준 3986번
from sys import stdin
N = int(input())
words = []
for i in range(N):
    for j in stdin.readline().split():
        words.append(j)

count = 0
for word in words:
    top = -1
    stack = [None for _ in range(len(word))]
    for ch in word:
        if -1 < top < len(word)-1 :
            if ch in stack:
                if ch == stack[top]:
                    stack[top] = None
                    top -=1
                else:
                    break
            else :
                top +=1
                stack[top] = ch
        else:
            top += 1
            stack[top] = ch

    if top == -1:
        count += 1
    else:
        count = count

print(count)




