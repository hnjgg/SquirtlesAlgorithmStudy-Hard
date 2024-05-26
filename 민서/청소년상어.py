input = open(0).readline
di = (-1, -1, 0, 1, 1, 1, 0, -1, -1, -1, 0, 1, 1, 1, 0, -1)
dj = (0, -1, -1, -1, 0, 1, 1, 1, 0, -1, -1, -1, 0, 1, 1, 1)
ans = 0
arrows = ["↑", "↖", "←", "↙", "↓", "↘", "→", "↗"]

def printarr(arr, fish_pos, fish_way):
    for i in range(4):
        for j in range(4):
            num = arr[i * 4 + j]
            arrow = arrows[fish_way[num]] if num != -1 and num != 0 else " "
            print(f"{num}{arrow}", end=' ')
        print()
    print()

def fish_turn(arr, i, j, way):
    for w in range(way, way + 8):
        ni, nj = i + di[w], j + dj[w]
        if not (0 <= ni < 4 and 0 <= nj < 4):
            continue
        if arr[ni * 4 + nj] == -1:
            continue
        return ni, nj, w % 8
    return i, j, way

def fish_move(arr, fish_pos, fish_way):
    for num in range(1, 17):
        if fish_pos[num] == -1:
            continue
        i, j, w = fish_pos[num] // 4, fish_pos[num] % 4, fish_way[num]
        ni, nj, nw = fish_turn(arr, i, j, w)
        if ni == i and nj == j:
            continue
        fish_way[num] = nw
        p, np = i * 4 + j, ni * 4 + nj
        a, b = arr[p], arr[np]
        arr[p], arr[np] = b, a
        if b != 0:
            fish_pos[b] = p
        fish_pos[a] = np
    return arr, fish_pos, fish_way

def shark(arr, fish_pos, fish_way, shark_pos, prey_pos, total):
    global ans
    prey_num = arr[prey_pos]
    total += prey_num
    if total > ans:
        ans = total
    shark_way = fish_way[prey_num]
    arr[shark_pos] = 0
    arr[prey_pos] = -1
    fish_pos[prey_num] = -1
    arr, fish_pos, fish_way = fish_move(arr, fish_pos, fish_way)
    i, j = prey_pos // 4, prey_pos % 4
    for k in range(1, 4):
        ni, nj = i + k * di[shark_way], j + k * dj[shark_way]
        if not (0 <= ni < 4 and 0 <= nj < 4) or arr[ni * 4 + nj] == 0:
            continue
        shark(arr[:], fish_pos[:], fish_way[:], i * 4 + j, ni * 4 + nj, total)

def main():
    arr = [0] * 16
    fish_pos = [0] * 17
    fish_way = [0] * 17
    pos = 0
    for _ in range(4):
        l = [*map(int, input().split())]
        for j in range(4):
            num, way = l[2 * j], l[2 * j + 1] - 1
            arr[pos] = num
            fish_pos[num] = pos
            fish_way[num] = way
            pos += 1
    shark(arr, fish_pos, fish_way, 0, 0, 0)
    print(ans)
    
main()
