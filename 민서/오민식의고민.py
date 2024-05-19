import heapq as hq
INF = 1<<30
input = open(0).readline

N, A, B, M = map(int, input().split())
graph = [[] for _ in range(N)]
graph2 = [[] for _ in range(N)]
for _ in range(M):
    s, t, c = map(int, input().split())
    graph[s].append((t, c))
edges = []
earn = [*map(int, input().split())]

flag = [False] * N
def dfs(s):
    if flag[s]:
        return
    flag[s] = True
    for t, c in graph[s]:
        graph2[t].append((s, c))
        dfs(t)
dfs(A)

flag = [False] * N
def dfs2(t):
    if flag[t]:
        return
    flag[t] = True
    for s, c in graph2[t]:
        edges.append((s, t, c))
        dfs2(s)
dfs2(B)

def bellmanford(A, B, N):
    cost = [INF] * N
    cost[A] = -earn[A]
    for _ in range(N):
        for u, v, w in edges:
            alt = cost[u] + w - earn[v]
            if alt < cost[v]:
                cost[v] = alt
    if cost[B] == INF:
        return INF
    for u, v, w in edges:
        if cost[u] + w - earn[v] < cost[v]:
            return -INF
    return cost[B]

ans = bellmanford(A, B, N)
if ans == INF:
    print("gg")
elif ans == -INF:
    print("Gee")
else:
    print(-ans)
