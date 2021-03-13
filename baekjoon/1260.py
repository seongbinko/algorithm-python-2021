import sys
from collections import deque

def bfs(graph,start, visited_bfs):

    q = deque([start]) # 1

    visited_bfs[start] = True

    while q:
        v = q.popleft()
        print(v, end=' ')
        for x in graph[v]:
            if not visited_bfs[x]: # 아직 방문하지 않았다면
                q.append(x)
                visited_bfs[x] = True

def dfs(graph,v, visited_dfs):

    visited_dfs[v] = True
    print(v, end=' ')
    
    for x in graph[v]:
        if not visited_dfs[x]:
             dfs(graph, x, visited_dfs)

global n
n,m,v = map(int,sys.stdin.readline().rstrip().split())

graph = [
    [] for _ in range(n+1)
]
visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

for _ in range(m):
    x, y = map(int,sys.stdin.readline().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(len(graph)):
    graph[i].sort() # 입력 되는 연결 정보가 오름차순으로 정리가 안되있어서 탐색은 되지만 출력에 문제가 있다.
                    # 그래서 sort 가 필요하다.

dfs(graph,v,visited_dfs)
print()
bfs(graph,v,visited_bfs)



