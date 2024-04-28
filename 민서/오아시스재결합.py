input = open(0).readline
stack = []
ans = 0
N = int(input())
for _ in range(N):
    n = int(input())
    same = 0
    while stack and stack[-1][0] <= n:
        last = stack.pop()
        ans += last[1]
        if last[0] == n:
            same += last[1]
    if stack:
        ans += 1
    if same > 0:
        stack.append((n, same + 1))
    else:
        stack.append((n, 1))
print(ans)
