from collections import deque

def bfs(s_r, s_c, visited, land):
    global R, C
    cnt = 0
    c_set = set()
    queue = deque()
    queue.append((s_r, s_c))
    visited[s_r][s_c] = 1
    c_set.add(s_c)
    cnt += 1
    

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                continue
            
            if visited[nr][nc] == 1 or land[nr][nc] == 0:
                continue
            
            queue.append((nr, nc))
            visited[nr][nc] = 1
            c_set.add(nc)
            cnt += 1

    return c_set, cnt


def solution(land):
    global R, C
    R = len(land)
    C = len(land[0])
    visited = [[0 for _ in range(C)] for _ in range(R)]
    available_list = [0 for _ in range(C)]

    for r in range(R):
        for c in range(C):
            if visited[r][c] == 0 and land[r][c] == 1:
                c_set, cnt = bfs(r, c, visited, land)
                for c in c_set:
                    available_list[c] += cnt

    answer = max(available_list)
    return answer