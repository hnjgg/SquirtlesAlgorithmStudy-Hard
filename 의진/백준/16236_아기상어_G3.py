import sys
import heapq
from collections import deque
from pprint import pprint
input = sys.stdin.readline

# Get Inputs
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# Set Up

# Initialize
fish_dict = {i: 0 for i in range(1, 7)}
fish_dict["available"] = 0
current_time = 0

shark_size = 2
eat_count = 0
dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

# Update States
for r in range(N):
    for c in range(N):
        if 1 <= board[r][c] <= 6:
            fish_dict[board[r][c]] += 1
        elif board[r][c] == 9:
            current_r = r
            current_c = c
            board[r][c] = 0

# Functions


def aggregate_dict(aggregate_num):
    global fish_dict
    fish_dict["available"] += fish_dict[aggregate_num]
    fish_dict[aggregate_num] = None


def is_available():
    global fish_dict
    return fish_dict["available"] > 0


def move(start_time, start_r, start_c):
    global shark_size, current_r, current_c, current_time, fish_dict, eat_count
    dq = deque()
    dq.append((start_time, start_r, start_c))
    visited = [[False] * N for _ in range(N)]
    visited[start_r][start_c] = True
    is_find = False
    while dq:
        time, r, c = dq.popleft()
        if 0 < board[r][c] < shark_size:
            dq.appendleft((time, r, c))
            is_find = True
            break

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            if visited[nr][nc]:
                continue

            if shark_size < board[nr][nc]:
                continue

            dq.append((time + 1, nr, nc))
            visited[nr][nc] = True

    if is_find:
        dq = sorted(list(dq))
        # print(dq)
        for item in dq:
            if 0 < board[item[1]][item[2]] < shark_size:
                dest = item
                current_r = dest[1]
                current_c = dest[2]
                current_time = dest[0]
                fish_dict["available"] -= 1
                board[current_r][current_c] = 0
                eat_count += 1
                break

        return True

    else:
        return False


aggregate_dict(1)
while True:
    # pprint(board)
    # print()
    if not is_available():
        print(current_time)
        break

    if not move(current_time, current_r, current_c):
        print(current_time)
        break

    if shark_size == eat_count:
        shark_size += 1
        eat_count = 0
        if shark_size <= 7:
            aggregate_dict(shark_size-1)
