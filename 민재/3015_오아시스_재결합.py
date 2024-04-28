import sys
input = sys.stdin.readline

n = int(input())

heights = []
for _ in range(n):
    heights.append(int(input()))


stack = [] # (height, cnt)

answer = 0

for h in heights:

    cnt = 1

    while stack and stack[-1][0] <= h:

        height, cnt = stack.pop()

        if height == h:
            answer += cnt
            cnt += 1

        elif height < h:
            answer += cnt
            cnt = 1

    if stack:
        answer += 1
    stack.append((h, cnt))

print(answer)

