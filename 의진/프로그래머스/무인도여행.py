from collections import deque
def solution(maps):
    maps = [list(m) for m in maps]
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    answer = []

    for r in range(len(maps)):
        for c in range(len(maps[0])):
            if maps[r][c] != 'X' and visited[r][c] == 0:
                answer.append(bfs((r, c), visited, maps))


    return sorted(answer) if answer else [-1]

def bfs(start, visited, maps):
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = 1
    result = 0
    while queue:
        # print(queue)
        r, c = queue.popleft()
        result += int(maps[r][c])
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if nr < 0 or nr >= len(maps) or nc < 0 or nc >= len(maps[0]):
                continue

            if visited[nr][nc] == 1:
                continue

            if maps[nr][nc] == 'X':
                continue

            queue.append((nr, nc))
            visited[nr][nc] = 1
    return result
    