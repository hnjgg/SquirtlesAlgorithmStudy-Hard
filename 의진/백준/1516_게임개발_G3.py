import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
times = [-1] * (N+1)
final_times = [-1] * (N+1)
indegrees = [-1] * (N+1)
graph = [[] for _ in range(N+1)]
q = deque()

for i in range(1, N+1):
    input_seq = list(map(int, input().split()))
    times[i] = input_seq[0]
    for node in input_seq[1:-1]:
        graph[node].append(i)
    indegrees[i] = len(input_seq[1:-1])

    if indegrees[i] == 0:
        final_times[i] = times[i]
        q.append((i, times[i]))

while q:
    node, time = q.popleft()
    for next_node in graph[node]:
        indegrees[next_node] -= 1
        final_times[next_node] = max(
            final_times[next_node], time + times[next_node])
        if indegrees[next_node] == 0:
            q.append((next_node, final_times[next_node]))

for final_time in final_times[1:]:
    print(final_time)
