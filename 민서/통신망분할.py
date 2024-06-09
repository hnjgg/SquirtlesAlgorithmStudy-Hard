import sys; sys.setrecursionlimit(1<<20)
input = open(0).readline
n_nodes = 0

def net_value(n):
    return n * (n - 1) // 2

def dfs(n):
    global n_nodes, graph, visited
    n_nodes += 1
    visited[n] = True
    for c in graph[n]:
        if not visited[c]:
            dfs(c)

def main():
    global n_nodes, graph, visited
    N, M, Q = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    edges = [(0, 0)]
    connect = [True] * (M + 1)
    for _ in range(M):
        X, Y = map(int, input().split())
        edges.append((X, Y))
    for _ in range(Q):
        connect[int(input())] = False
    for i in range(1, M + 1):
        if connect[i]:
            X, Y = edges[i]
            graph[X].append(Y)
            graph[Y].append(X)
    group = []
    for i in range(N + 1):
        if visited[i]:
            continue
        dfs(i)
        group.append(n_nodes)
        n_nodes = 0
    after = 0
    for g in group:
        after += net_value(g)
    print(net_value(N) - after)

main()
