import sys
import copy
input = sys.stdin.readline
INF = int(1e9)


def bf(start):
    dist[start] = 0

    for i in range(2*N):
        for j in range(M):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]

            if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost
                if i >= N-1:
                    dist[next_node] = -INF


N, start, dest, M = map(int, input().split())
init_edges = [tuple(map(int, input().split())) for _ in range(M)]
earnings = list(map(int, input().split()))
edges = []
for init_edge in init_edges:
    departure = init_edge[0]
    arrival = init_edge[1]
    cost = init_edge[2] - earnings[arrival]
    edges.append((departure, arrival, cost))
dist = [INF] * (N+1)
bf(start, dest)

if dist[dest] == INF:
    print("gg")

elif dist[dest] == -INF:
    print("Gee")

else:
    print(earnings[start]-dist[dest])
