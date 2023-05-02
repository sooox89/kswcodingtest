# Tree_list

n = 5
graph = [[] for _ in range(n+1)]

graph[1] = [2,3]
graph[2] =[]
graph[3] = [4,5]
graph[4] = []
graph[5] = []

from collections import deque
def BFS(graph, idx, visited):
    queue = deque()
    queue.append(idx)

    while queue:
        current = queue.popleft()

        if not visited[current]:
            print(current)
            visited[current] = True

            for child in graph[current]:
                queue.append(child)

print('BFS result')
visited = [False]*(n+1)
BFS(graph,1,visited)
# 1 -2 -5
#   -3 -4