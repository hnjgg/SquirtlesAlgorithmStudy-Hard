# 메모리 : 150928KB
# 시간 : 940ms

import sys

input = sys.stdin.readline
q = []

N, K = map(int, input().split())


def bfs(start_x):
    global K
    mov = 1
    visited = set()
    q = []
    q.append(start_x)
    visited.add((0, start_x))
    stop = False

    while q:
        new_q = []

        # 1 time step부터
        K += mov
        if K > 500_000:
            return -1
        # 만약 1 time step, 같은 홀짝수에 x가 이미 방문을 했다면? -> 동생 만나기 가능
        if (mov % 2, K) in visited:
            return mov

        for x in q:
            for nx in [x-1, x+1, 2*x]:
                # 아직 방문을 안했었으나 1 timestep으로 x가 이동하면서 동생이랑 만나면 -> 동생 만나기 가능
                if nx == K:
                    return mov
                if nx < 0 or nx > 500_000:
                    continue
                if (mov % 2, nx) in visited:
                    continue
                new_q.append(nx)
                visited.add((mov % 2, nx))
        q = new_q
        mov += 1


if N == K:
    print(0)
else:
    print(bfs(N))
