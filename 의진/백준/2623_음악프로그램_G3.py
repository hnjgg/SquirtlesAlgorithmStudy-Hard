from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
order_info = [list(map(int, input().split())) for _ in range(M)]

require = [set() for _ in range(N+1)]
require_rev = [set() for _ in range(N+1)]
len_info = {}
visited = [False] * (N+1)
zero_q = deque()

for pd in order_info:
    for i in range(1, len(pd)-1):
        require[pd[i+1]].add(pd[i])
        require_rev[pd[i]].add(pd[i+1])

for idx, item in enumerate(require[1:]):
    idx += 1
    if len(item) == 0:
        zero_q.append(idx)

result = []
while zero_q:
    item = zero_q.popleft()
    visited[item] = True
    result.append(item)

    for next_node in require_rev[item]:
        require[next_node].remove(item)
        if len(require[next_node]) == 0:
            zero_q.append(next_node)

if False not in visited[1:]:
    for item in result:
        print(item)
else:
    print(0)
