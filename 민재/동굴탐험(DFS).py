def dfs(v, graph, visited, checked, key, locked, que):
    if visited[v]:
        return
    
    if locked[v]:
        checked[v] = True
        return
    
    visited[v] = True

    if key[v] != -1:
        locked[key[v]] = False
        que.append(key[v])

    
    for c in graph[v]:
        dfs(c, graph, visited, checked, key, locked, que)



def solution(n, path, order):
    graph = [[] for i in range(n)]
    key = [-1 for i in range(n)]
    locked = [False for i in range(n)]

    visited = [False for i in range(n)]
    checked = [False for i in range(n)]

    for src, dest in path:
        graph[src].append(dest)
        graph[dest].append(src)

    for src, dest in order:
        key[src] = dest
        locked[dest] = True

    que = [0]
    checked[0] = True
    
    while que:
        new_que = []
        for v in que:
            if not checked[0]: continue
            dfs(v, graph, visited, checked, key, locked, new_que)
        
        que = new_que
        
        



