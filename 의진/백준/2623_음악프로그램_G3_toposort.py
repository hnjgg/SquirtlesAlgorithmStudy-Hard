from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
order_info = [list(map(int, input().split())) for _ in range(M)]

queue = deque()
indegrees = [0] * (N+1)
graph = [0] + [[] for _ in range(N)]

for pd in order_info:
    for i in range(1, len(pd)-1):
        graph[pd[i]].append(pd[i+1])
        indegrees[pd[i+1]] += 1

for idx, indegree in enumerate(indegrees[1:]):
    idx += 1
    if indegree == 0:
        queue.append(idx)

cnt = 0
result = []

while queue:
    # print(queue)
    cnt += 1
    node = queue.popleft()
    result.append(node)
    for next_node in graph[node]:
        indegrees[next_node] -= 1
        if indegrees[next_node] == 0:
            queue.append(next_node)
    graph[node] = []

if cnt == N:
    for node in result:
        print(node)
else:
    print(0)
