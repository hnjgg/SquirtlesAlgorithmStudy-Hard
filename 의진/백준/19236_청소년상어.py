import sys
input = sys.stdin.readline
number = [[0] * 4 for _ in range(4)]
direction = [[0] * 4 for _ in range(4)]
fish_pos = {0: "dead"}
shark_pos = []
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]

# Fish 정보 초기화
for i in range(4):
    info = list(map(int, input().split()))
    for j, item in enumerate(info):
        if j % 2 == 0:
            number[i][j//2] = item
            fish_pos[item] = (i, j//2)
        else:
            direction[i][j//2] = item-1


def update_fish(fish_num):
    global shark_pos
    # print(fish_pos)
    if fish_pos[fish_num] == "dead":
        return None
    r, c = fish_pos[fish_num]
    # print(fish_num, r, c)
    first_direction = direction[r][c]
    for _ in range(8):
        nr = r + dr[direction[r][c]]
        nc = c + dc[direction[r][c]]

        if nr < 0 or nr >= 4 or nc < 0 or nc >= 4:
            direction[r][c] = (direction[r][c]+1) % 8
            continue

        elif shark_pos == [nr, nc]:
            direction[r][c] = (direction[r][c]+1) % 8
            continue

        else:
            if fish_pos[number[nr][nc]] != "dead":
                fish_pos[fish_num] = (nr, nc)
                fish_pos[number[nr][nc]] = (r, c)
                state = "Not Dead"
            else:
                fish_pos[number[r][c]] = (nr, nc)
                state = "Dead"
            number[nr][nc], number[r][c] = number[r][c], number[nr][nc]
            direction[nr][nc], direction[r][c] = direction[r][c], direction[nr][nc]

            return (r, c, nr, nc, first_direction, state)

    return None


def update_all_fishes():
    history_stack = []
    for num in range(1, 17):
        history = update_fish(num)
        # print(number, direction)
        if history is not None:
            history_stack.append(history)
    # print("==========================")

    return history_stack


def revert_fish(history):
    r = history[0]
    c = history[1]
    nr = history[2]
    nc = history[3]
    first_direction = history[4]
    state = history[5]

    if state == "Not Dead":
        fish_pos[number[r][c]], fish_pos[number[nr][nc]
                                         ] = fish_pos[number[nr][nc]], fish_pos[number[r][c]]
    else:
        fish_pos[number[nr][nc]] = (r, c)
    number[nr][nc], number[r][c] = number[r][c], number[nr][nc]
    direction[nr][nc], direction[r][c] = direction[r][c], direction[nr][nc]
    direction[r][c] = first_direction


def revert_all_fishes(history_stack):
    while history_stack:
        history = history_stack.pop()
        revert_fish(history)


max_score = 0


def dfs(shark_r, shark_c, current_sum):
    global max_score
    global shark_pos
    # 1. 먹는다.
    shark_pos = [shark_r, shark_c]
    past_number = number[shark_r][shark_c]
    shark_direction = direction[shark_r][shark_c]
    past_fish_pos = fish_pos[number[shark_r][shark_c]]

    number[shark_r][shark_c] = 0
    fish_pos[past_number] = "dead"
    current_sum += past_number

    max_score = max(current_sum, max_score)

    # 2. 물고기가 이동한다.
    # print(current_sum)
    history_stack = update_all_fishes()

    # 3. 상어가 이동한다.
    n_shark_r = shark_r
    n_shark_c = shark_c

    while True:
        n_shark_r += dr[shark_direction]
        n_shark_c += dc[shark_direction]

        if n_shark_r < 0 or n_shark_r >= 4 or n_shark_c < 0 or n_shark_c >= 4:
            break
        if number[n_shark_r][n_shark_c] != 0:
            dfs(n_shark_r, n_shark_c, current_sum)

    # 4. 물고기 원위치
    revert_all_fishes(history_stack)

    # 5. 먹은 물고기 원위치
    number[shark_r][shark_c] = past_number
    fish_pos[number[shark_r][shark_c]] = past_fish_pos
    current_sum -= past_number


dfs(0, 0, 0)
print(max_score)
# print(number)
