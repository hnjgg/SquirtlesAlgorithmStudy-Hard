import sys
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))

seq2cnt = {}

for element in seq:
    if seq2cnt.get(element) is not None:
        seq2cnt[element] += 1
    else:
        seq2cnt[element] = 1

ngf = [-1] * N
stack = []

for idx, value in enumerate(seq):
    element = seq2cnt[value]
    if not stack:
        stack.append((element, idx))

    if stack[-1][0] >= element:
        stack.append((element, idx))

    elif stack[-1][0] < element:
        item = stack.pop()
        ngf[item[1]] = value
        stack.append((element, idx))

        while True:
            if len(stack) == 1:
                break
            elif stack[-2][0] < element:
                temp = stack.pop()
                item = stack.pop()
                ngf[item[1]] = value
                stack.append(temp)
            else:
                break

for item in ngf:
    print(item, end=" ")
