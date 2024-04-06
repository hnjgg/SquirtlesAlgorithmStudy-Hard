from collections import deque

def solution(n, path, order):
    answer = True
    
    graph = [[] for i in range(n)]
    lock = [0 for i in range(n)]
    # index: 목적지, value: 선수방문해야하는 곳

    for p in path:
        u = p[0]
        v = p[1]
        graph[u].append(v)
        graph[v].append(u)
    
    for orde in order:
        needed = orde[0]
        to = orde[1]
        lock[to] = needed

    visited = [False for i in range(n)]
    q = deque([0])
    visited[0] = True

    waiting = {} # 방문순서 안지키고 먼저 온 애들 보류시키는 곳
    # key: 선수 방문
    # value: 그 다음 행선지
    
    while q:
        curr = q.popleft()

        # 선수방문해야할 곳이 있는데, 그곳을 아직 방문안했다?
        if lock[curr] and not visited[lock[curr]]:
            # 보류 후 continue
            waiting[lock[curr]] = curr
            continue

        visited[curr] = True


        for v in graph[curr]:
            if not visited[v]:
                q.append(v)

        # 지금 방문하는 곳이 waiting에 포함되어 있다면
        # 이제 현재 위치를 방문해야 갈 수 있는 정점으로 이동가능하므로
        # 이동가능한 정점을 q에 넣어준다.

        if curr in waiting:
            q.append(waiting[curr])

            
    for visit in visited:
        if not visit:
            answer = False
            break
    
    # print(answer)
    return answer


solution(9,
         [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]],
         [[8,5],[6,7],[4,1]])

solution(
    9, 
    [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]],
    [[4,1],[5,2]]
)

solution(
    9, 
    [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]],
    [[4,1],[8,7],[6,5]]
)