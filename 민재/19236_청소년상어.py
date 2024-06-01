import copy

max_answer = 0
fish_live = {}
fish_number = [[0 for _ in range(4)] for _ in range(4)]
fish_direction = [[0 for _ in range(4)] for _ in range(4)]

arrows = ["↑", "↖", "←", "↙", "↓", "↘", "→", "↗"]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]


for i in range(4):
    line = list(map(int, input().split()))
    for j in range(8):
        if j % 2 == 0:
            fish_number[i][j // 2] = line[j]
            
            # key: number, value: [y,x]
            fish_live[line[j]] = [i, j // 2] 
        else: 
            fish_direction[i][j // 2] = line[j] - 1


def printArr(fish_number, fish_direction):
    for i in fish_number:
        for j in i:
            print(j, end=" ")
        print()

    print("=====================")

    for i in fish_direction:
        for j in i:
            print(arrows[j], end=" ")
        print()



def process(shark_y, shark_x, curr_sum, fish_live, fish_number, fish_direction):
    global max_answer
    # print(shark_y, shark_x, "냠냠 !! ㅋㅋㅋ")
    init_fish = copy.deepcopy(fish_number)
    init_fish_dir = copy.deepcopy(fish_direction)
    init_fish_live = copy.deepcopy(fish_live)

    # 1. 상어가 물고기를 먹는다.
    eaten_fish_number = fish_number[shark_y][shark_x]
    shark_direction = fish_direction[shark_y][shark_x]

    fish_number[shark_y][shark_x] = 0
    fish_live[eaten_fish_number] = False

    curr_sum += eaten_fish_number

    max_answer = max(max_answer, curr_sum)

    # print("=====BEFORE======")
    # printArr(fish_number, fish_direction)

    # 2. 물고기를 이동시킨다.

    for num in range(1, 17):
        if fish_live[num] != False:
            curr_y, curr_x = fish_live[num]
            # print("이동 ? ", num, curr_y, curr_x)
            for _ in range(8):
                # print(arrows[fish_direction[curr_y][curr_x]])
                ndy = dy[fish_direction[curr_y][curr_x]]
                ndx = dx[fish_direction[curr_y][curr_x]]

                nposy = curr_y + ndy
                nposx = curr_x + ndx

                if nposy >= 4 or nposy < 0 or nposx >= 4 or nposx < 0:
                    fish_direction[curr_y][curr_x] = (fish_direction[curr_y][curr_x] + 1) % 8
                    continue

                if nposy == shark_y and nposx == shark_x:
                    fish_direction[curr_y][curr_x] = (fish_direction[curr_y][curr_x] + 1) % 8
                    continue

                if fish_number[nposy][nposx] != 0:
                    fish_live[fish_number[nposy][nposx]] = [curr_y, curr_x]
                    fish_live[num] = [nposy, nposx]

                    fish_number[nposy][nposx], fish_number[curr_y][curr_x] = fish_number[curr_y][curr_x], fish_number[nposy][nposx]
                    fish_direction[nposy][nposx], fish_direction[curr_y][curr_x] = fish_direction[curr_y][curr_x], fish_direction[nposy][nposx]
                    break
                else:
                # elif fish_number[nposy][nposx] == -1:
                    fish_number[nposy][nposx] = fish_number[curr_y][curr_x]
                    fish_number[curr_y][curr_x] = 0
                    fish_direction[nposy][nposx] = fish_direction[curr_y][curr_x]
                    fish_direction[curr_y][curr_x] = 0
                    fish_live[num] = [nposy, nposx]
                    break
            # printArr(fish_number, fish_direction)
    
    # print("=====AFTER======")
    # printArr(fish_number, fish_direction)

    # 3. 상어가 이동한다.
    nsharky = shark_y
    nsharkx = shark_x
    while True:
        nsharky += dy[shark_direction]
        nsharkx += dx[shark_direction]
        
        if nsharky >= 4 or nsharky < 0 or nsharkx >= 4 or nsharkx < 0:
            break
        if fish_number[nsharky][nsharkx] != 0:
            process(nsharky, nsharkx, curr_sum, copy.deepcopy(fish_live), copy.deepcopy(fish_number), copy.deepcopy(fish_direction))

    # 4. 상어가 먹은 물고기 포함, 물고기를 원래 위치로 초기화시킨다.
    fish_number = init_fish
    fish_direction = init_fish_dir
    fish_live = init_fish_live
    
    curr_sum -= eaten_fish_number

process(0, 0, 0, fish_live, fish_number, fish_direction)

print(max_answer)