n = 5

# 6x6 행렬 만들기 -> 각 0번째 idx 사용을 안할 것임
matrix =[[0]*(n+1) for _ in range(n+1)]

matrix[1][2]=1
matrix[2][1]=1


matrix[1][3]=1
matrix[3][1]=1

matrix[3][4]=1
matrix[4][3]=1

matrix[2][5]=1
matrix[5][2]=1

from collections import deque

def BFS(matrix, idx, visited):
    queue = deque()
    queue.append(idx)

    while queue:
        current = queue.popleft()

        if not visited[current]:
            print(current)
            visited[current] = True

        for child in range(len(matrix[current])):
            if matrix[current][child] ==1 and not visited[child]:
                queue.append(child)

print('BFS result')
visited = [False]*(n+1)
BFS(matrix,1,visited)
def DFS(matrix, idx, visited):
    stack = [idx]
    visited[idx] = True

    while stack:
        current = stack.pop()

        if not visited[current]:
            print(current)
            visited[current] = True

        for child in range(len(matrix[current])-1,-1,-1):
            if matrix[current][child] ==1 and not visited[child]:
                stack.append(child)

print('DFS result')
visited = [False]*(n+1)
DFS(matrix,1, visited)

# 차이를 보여주기 위해 .