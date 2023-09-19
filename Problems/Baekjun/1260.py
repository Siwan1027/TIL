# baekjun problem no.1260

import sys
from collections import deque

# 정점, 간선, 시작점
n, m, v = map(int,sys.stdin.readline().split())

# 원소의 개수가 n개에 맞춰 그래프로 표현할 리스트를 생성
# 딕셔너리형으로 만드는 것이 더 효율적이지 않을까?
graph = [[] for _ in range(n+1)]

# 그래프 생성
# 간선의 개수 = 서로 연결된 노드의 수
# 즉 모든 연결된 경우를 리스트에 append 하여 그래프 형태를 list화
for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

# 깊이 우선 탐색
def dfs(graph, v, visited):
    # 방문 여부를 T/F 형으로 저장
    visited[v] = True
    print(v, end=' ')
    for j in  graph[v]:
        if not visited[j]:
            dfs(graph, j, visited)
    # 방문기록 초기화
    # 왜 함수 안에 초기화하면 안되지?
    # visited = [False] * (n+1)

# 너비 우선 탐색
def bfs(graph, v, visited):
    # queue 생성
    q = deque([v])
    # 시작 지점을 방문 처리
    visited[v] = True
    # 큐를 비울 때까지 반복
    while q:
        # 시작점을 pop 및 출력
        current_v = q.popleft()
        print(current_v, end = ' ')

        for k in graph[current_v]:
            if not visited[k]:
                q.append(k)
                visited[k] = True
    # 방문기록 초기화
    # visited = [False] * (n+1)

visited = [False] * (n+1)
dfs(graph, v, visited)
print("")
visited = [False] * (n+1)
bfs(graph,v, visited)