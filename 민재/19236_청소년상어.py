max_answer = 0
fish_live = {0: False}
fish_number = [[0 for _ in range(4)] for _ in range(4)]
fish_direction = [[0 for _ in range(4)] for _ in range(4)]
shark_pos = [0, 0] # [y, x]

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


def printArr():
    for i in fish_number:
        for j in i:
            print(j, end=" ")
        print()

    print("=====================")

    for i in fish_direction:
        for j in i:
            print(arrows[j], end=" ")
        print()

print(fish_live)


def process(shark_y, shark_x, curr_sum, fish_live, fish_number, fish_direction):
    global max_answer
    # 1. 상어가 물고기를 먹는다.
    shark_direction = fish_direction[shark_y][shark_x]
    fish_live[fish_number[shark_y][shark_x]] = False
    curr_sum += fish_number[shark_y][shark_x]

    max_answer = max(max_answer, curr_sum)

    # 2. 물고기를 이동시킨다.
    for num in range(1, 17):
        if fish_live[num] != False:
            
            curr_y, curr_x = fish_live[num]
            print("이동 ? ", num, curr_y, curr_x)

            while True:
                curr_dir = fish_direction[curr_y][curr_x]
                print(arrows[curr_dir])
                ndy = dy[curr_dir]
                ndx = dx[curr_dir]

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
                elif fish_number[nposy][nposx] == 0:
                    fish_number[nposy][nposx] = fish_number[curr_y][curr_x]
                    fish_number[curr_y][curr_x] = 0
                    fish_direction[curr_y][curr_x] = 0
                    fish_live[num] = [nposy, nposx]
                    break
            printArr()
            print()
    
    printArr()
                





    # 3. 상어가 이동한다.

    # 4. 물고기를 원래 위치로 초기화시킨다.

    # 5. #1에서 상어가 먹은 물고기도 원위치시킨다.

process(0, 0, 0, fish_live, fish_number, fish_direction)