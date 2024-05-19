from collections import deque
input = open(0).readline
INF = 1<<30
dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]
N = int(input())
arr = [[0] * N for _ in range(N)]
for i in range(N):
    for j, n in enumerate(input().split()):
        arr[i][j] = n = int(n)
        if n == 9:
            arr[i][j] = 0
            R, C = i, j
def bfs(sr, sc, shark):
    fr, fc, ft = N, N, INF
    visited = [[0] * N for _ in range(N)]
    visited[sr][sc] = 1
    que = deque()
    que.append((sr, sc, 0))
    while len(que):
        r, c, t = que.popleft()
        for i in range(4):
            nr, nc, nt = r+dr[i], c+dc[i], t+1
            if (not (0<=nr<N and 0<=nc<N) or
                arr[nr][nc] > shark or
                visited[nr][nc] == 1):
                continue
            visited[nr][nc] = 1
            que.append((nr, nc, nt))
            if 0 < arr[nr][nc] < shark:
                if nt < ft or (nt == ft and (nr < fr or (nr == fr and nc < fc))):
                    fr, fc, ft = nr, nc, nt
    return fr, fc, ft
def sol(r, c, shark, feed):
    ans = 0
    while True:
        r, c, t = bfs(r, c, shark)
        if t == INF:
            return ans
        else:
            arr[r][c] = 0
            ans += t
            feed += 1
            if feed == shark:
                shark += 1
                feed = 0
print(sol(R, C, 2, 0))
