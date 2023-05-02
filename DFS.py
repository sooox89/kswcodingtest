# Tree list / DFS
n = 5
graph = [[] for _ in range(n+1)]

graph[1] = [2,3]
graph[2] =[]
graph[3] = [4,5]
graph[4] = []
graph[5] = []

visited = [False]*(n+1)
def DFS(graph, idx, visited):
    stack = [idx]
    visited[idx] = True

    while stack:
        current = stack.pop()

        if not visited[current]:
            print(current)
            visited[current] = True

        for child in graph[current]:
            if not visited[child]:
                stack.append(child)

DFS(graph=graph,idx=1, visited=visited)

# Tree_matrix / DFS
# n = 5
#
# # 6x6 행렬 만들기 -> 각 0번째 idx 사용을 안할 것임
# matrix =[[0]*(n+1) for _ in range(n+1)]
#
# matrix[1][2]=1
# matrix[2][1]=1
#
#
# matrix[1][3]=1
# matrix[3][1]=1
#
# matrix[3][4]=1
# matrix[4][3]=1
#
# matrix[3][5]=1
# matrix[5][3]=1
#
# visited = [False]*(n+1)
#
# def DFS(matrix, idx, visited):
#     stack = [idx]
#     visited[idx] = True
#
#     while stack:
#         current = stack.pop()
#
#         if not visited[current]:
#             print(current)
#             visited[current] = True
#
#         for child in range(len(matrix[current])-1,-1,-1):
#             if matrix[current][child] ==1 and not visited[child]:
#                 stack.append(child)
#
# DFS(matrix,1, visited)
