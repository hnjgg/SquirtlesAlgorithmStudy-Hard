import sys
input = sys.stdin.readline

N = int(input())
line = [int(input()) for _ in range(N)]
stack = []
answer = 0

for person in line:
    while True:
        if not stack:
            stack.append([person, 1])
            break
        else:
            if stack[-1][0] < person:
                answer += stack[-1][1]
                stack.pop()
            elif stack[-1][0] == person:
                answer += stack[-1][1]
                stack[-1][1] += 1
                if len(stack) > 1:
                    answer += 1
                break
            else:
                answer += 1
                stack.append([person, 1])
                break

print(answer)
