import copy

max_answer = 0
fish_live = {}
fish_number = [[-1 for _ in range(4)] for _ in range(4)]
fish_direction = [[0 for _ in range(4)] for _ in range(4)]

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]

# 입력 받기
for i in range(4):
    line = list(map(int, input().split()))
    for j in range(8):
        if j % 2 == 0:
            fish_number[i][j // 2] = line[j]
            fish_live[line[j]] = [i, j // 2]
        else:
            fish_direction[i][j // 2] = line[j] - 1

def process(shark_y, shark_x, curr_sum, fish_live, fish_number, fish_direction):
    global max_answer

    # 현재 상태 복사
    fish_number_copy = copy.deepcopy(fish_number)  # 상태 복사
    fish_direction_copy = copy.deepcopy(fish_direction)  # 상태 복사
    fish_live_copy = copy.deepcopy(fish_live)  # 상태 복사

    # 1. 상어가 물고기를 먹는다.
    curr_sum += fish_number_copy[shark_y][shark_x]
    shark_direction = fish_direction_copy[shark_y][shark_x]
    fish_live_copy[fish_number_copy[shark_y][shark_x]] = False
    fish_number_copy[shark_y][shark_x] = -1

    max_answer = max(max_answer, curr_sum)

    # 2. 물고기를 이동시킨다.
    for num in range(1, 17):
        if fish_live_copy.get(num):
            curr_y, curr_x = fish_live_copy[num]
            direction = fish_direction_copy[curr_y][curr_x]
            for _ in range(8):
                ny, nx = curr_y + dy[direction], curr_x + dx[direction]
                if 0 <= ny < 4 and 0 <= nx < 4 and (ny != shark_y or nx != shark_x):
                    if fish_number_copy[ny][nx] != -1:
                        fish_live_copy[fish_number_copy[ny][nx]] = [curr_y, curr_x]
                    fish_number_copy[ny][nx], fish_number_copy[curr_y][curr_x] = fish_number_copy[curr_y][curr_x], fish_number_copy[ny][nx]
                    fish_direction_copy[ny][nx], fish_direction_copy[curr_y][curr_x] = fish_direction_copy[curr_y][curr_x], fish_direction_copy[ny][nx]
                    fish_live_copy[num] = [ny, nx]
                    break
                direction = (direction + 1) % 8
            fish_direction_copy[curr_y][curr_x] = direction

    # 3. 상어가 이동한다.
    ny, nx = shark_y, shark_x
    while True:
        ny += dy[shark_direction]
        nx += dx[shark_direction]
        if 0 <= ny < 4 and 0 <= nx < 4:
            if fish_number_copy[ny][nx] != -1:
                process(ny, nx, curr_sum, fish_live_copy, fish_number_copy, fish_direction_copy)  # 재귀 호출 시 복사본 사용
        else:
            break

# 초기 상어 위치에서 시작
process(0, 0, 0, fish_live, fish_number, fish_direction)
print(max_answer)
