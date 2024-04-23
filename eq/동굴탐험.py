import sys
sys.setrecursionlimit(100_000_000)


def dfs(n, graph, visited, checked, key, locked, que):
    if visited[n]:
        return
    if locked[n]:
        checked[n] = True
        return
    visited[n] = True
    if key[n] != -1:
        locked[key[n]] = False
        que.append(key[n])
    for c in graph[n]:
        dfs(c, graph, visited, checked, key, locked, que)

def solution(N, path, order):
    graph = [[] for _ in range(N)]
    visited = [False] * N
    checked = [False] * N
    key = [-1] * N
    locked = [False] * N
    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)
    for a, b in order:
        key[a] = b
        locked[b] = True
    que = [0]
    checked[0] = True
    while que:
        new_que = []
        for n in que:
            if not checked[n]:
                continue
            dfs(n, graph, visited, checked, key, locked, new_que)
        que = new_que
    return sum(visited) == N

if __name__ == "__main__":
    solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]])
    solution(9, [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]], [[4,1],[5,2]])
    solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[4,1],[8,7],[6,5]])
