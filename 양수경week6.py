graph_list = {
    0 : set([1]),
    1 : set([0,2,3]),
    2 : set([1,3,4]),
    3 : set([1,2,4,5]),
    4 : set([2,3]),
    5 : set([3,6,7]),
    6 : set([5,8]),
    7 : set([5]),
    8 : set([6])
}
root = 0

from collections import deque

def BFS(graph, root):
    visited = []
    # 값을 저장할 변수나 자료형 여기서 선언할 것
    queue = deque([root])

    while queue:
        # 1. 큐에서 처리할 노드 가져오기
        current= queue.popleft()
        # 2. 헤당 노드가 방문 되었었는지 확인할 것
        if current not in visited:
            # 3. 방문했다고 기록
            visited.append(current)

            queue += graph[current] - set(visited)
            # 여기서 방문된 상태이다.

            # 필요한 처리를 해주세요 // current 노드를 가지고 필요한 처리 진행
    return visited

def DFS(graph,root):
    visited = []
    stack = [root]

    while stack:
        # 1. 스택에서 처리할 노드 가져오기
        current = stack.pop()

        # 2. 해당 노드가 방문되었었는지 확인할 것
        if current not in visited:
            # 3. 방문했다고 기록
            visited.append(current)
            stack += graph[current] - set(visited)
            # 방문된 상태에서 문제가 요구하는 처리를 진행할 것
    return visited

print(BFS(graph_list,root))

print(DFS(graph_list,root))


