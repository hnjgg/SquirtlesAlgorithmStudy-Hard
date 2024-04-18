import sys
input = sys.stdin.readline

N = int(input())
line = [int(input()) for _ in range(N)]

if N == 1:
    answer = 0
else:
    stack = [[line[0], 1]]
    cnt = 1
    answer = N - 1

    for person in line[1:]:
        if stack[-1][0] > person:
            stack.append([person, 1])

        elif stack[-1][0] == person:
            stack[-1][1] += 1

        else:
            while True:
                answer += stack[-1][1]
                stack.pop()
                if not stack or stack[-1][0] > person:
                    stack.append([person, 1])
                    break
                elif stack[-1][0] == person:
                    stack[-1][1] += 1
                    break


print(answer)
