import sys
input = sys.stdin.readline

sys.setrecursionlimit(1_000_000)

N = int(input())
buildings = list(map(int, input().split()))

stack = []
info = [0] + [[-1, -1] for _ in range(N)]

for idx, building in enumerate(buildings):
    while True:
        if not stack:
            stack.append((building, idx + 1))
            break
        else:
            if stack[-1][0] < building:
                prev = stack.pop()
                info[prev[1]][1] = idx + 1
            else:
                info[idx + 1][0] = stack[-1][1]
                stack.append((building, idx + 1))
                break

ans_list = [0] + [[-1, -1, 100001] for _ in range(N)]


def dfs_left(current):
    if ans_list[current][0] == -1:
        if info[current][0] == -1:
            ans_list[current][0] = 0
        else:
            cnt = dfs_left(info[current][0])
            if buildings[info[current][0] - 1] == buildings[current - 1]:
                ans_list[current][0] = cnt
            else:
                ans_list[current][0] = cnt + 1

    if info[current][0] != -1:
        if buildings[info[current][0] - 1] == buildings[current - 1]:
            ans_list[current][2] = ans_list[info[current][0]][2]
        else:
            ans_list[current][2] = info[current][0]

    return ans_list[current][0]


def dfs_right(current):
    if info[current][0] == -1 and info[current][1] != -1:
        ans_list[current][2] = info[current][1]

    elif info[current][1] != -1 and \
            abs(current - ans_list[current][2]) > abs(current - info[current][1]):
        ans_list[current][2] = info[current][1]

    if ans_list[current][1] == -1:
        if info[current][1] == -1:
            ans_list[current][1] = 0
        else:
            cnt = dfs_right(info[current][1])
            ans_list[current][1] = cnt + 1
    return ans_list[current][1]


for idx, building in enumerate(buildings):
    dfs_left(idx + 1)
    dfs_right(idx + 1)

for item in ans_list[1:]:
    ans = item[0] + item[1]
    if ans == 0:
        print(ans)
    else:
        print(ans, item[2])
