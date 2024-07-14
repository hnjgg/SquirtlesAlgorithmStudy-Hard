import sys
import heapq
# from pprint import pprint
input = sys.stdin.readline

INF = 1 << 30
N = int(input())
planets = []

for idx in range(N):
    pos = tuple(map(int, input().split()))
    planets.append([idx, pos])  # [idx, pos, root]

x_sort_planets = sorted(planets, key=lambda x: x[1][0])
y_sort_planets = sorted(planets, key=lambda x: x[1][1])
z_sort_planets = sorted(planets, key=lambda x: x[1][2])

candidate_edges = []
parent = list(range(N))


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for axis, sorted_planets in enumerate([x_sort_planets, y_sort_planets, z_sort_planets]):
    for i in range(len(sorted_planets)-1):
        left = min(sorted_planets[i][0], sorted_planets[i+1][0])
        right = max(sorted_planets[i][0], sorted_planets[i+1][0])
        edge = (abs(sorted_planets[i][1][axis] -
                sorted_planets[i+1][1][axis]), left, right)
        heapq.heappush(candidate_edges, edge)

cnt = 0
ans = 0
while cnt < N-1:
    edge = heapq.heappop(candidate_edges)
    if find_parent(parent, edge[1]) != find_parent(parent, edge[2]):
        ans += edge[0]
        cnt += 1
        union_parent(parent, edge[1], edge[2])

print(ans)
