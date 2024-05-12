input = open(0).readline

def dfs(n):
    if ans[n] != -1:
        return ans[n]
    mx = 0
    for c in graph[n]:
        alt = dfs(c)
        if alt > mx:
            mx = alt
    ans[n] = mx + time[n]
    return ans[n]

N = int(input())
graph = [[] for _ in range(N + 1)]
time = [0] * (N + 1)
ans = [-1] * (N + 1)
for i in range(1, N + 1):
    l = [*map(int, input().split())]
    time[i] = l[0]
    for n in l[1:-1]:
        graph[i].append(n)
for i in range(1, N + 1):
    print(dfs(i))
