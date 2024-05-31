from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]


for _ in range(M):
    numbers = list(map(int, input().split()))
    
    n = numbers[0]
    numbers = numbers[1:]
    for i in range(1, n):
        graph[numbers[i-1]].append(numbers[i])

indegrees = [0 for _ in range(N+1)]
for idx, gra in enumerate(graph):
    for node in gra:
        indegrees[node] += 1


q = deque()
for idx, indegree in enumerate(indegrees):
    if idx == 0: continue
    if indegree == 0:
        q.append(idx)


answer = []
while q:

    curr = q.popleft()
    answer.append(curr)

    for v in graph[curr]:
        indegrees[v] -= 1

        if indegrees[v] == 0:
            q.append(v)

if len(answer) != N:
    print(0)
else:
    for ans in answer:
        print(ans)