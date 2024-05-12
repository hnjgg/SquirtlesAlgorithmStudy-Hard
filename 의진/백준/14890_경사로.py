import sys
input = sys.stdin.readline

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

ans = 0
# ans_list = []

# 가로 방향 체크
for row_num in range(N):
    is_possible_list = [False] + [True] * N + [False]
    is_passed = True
    for i in range(1, N):
        front = board[row_num][i-1]
        rear = board[row_num][i]
        if abs(front - rear) >= 2:
            is_passed = False
            break
        if rear - front == 1:  # 1 증가
            if False in is_possible_list[max(0, i+1-L): i+1]:
                is_passed = False
                break
            else:
                is_possible_list[max(0, i+1-L): i+1] = [False] * \
                    (i+1 - max(0, i+1-L))
        elif front - rear == 1:  # 1 감소
            if False in is_possible_list[i+1: min(i+L+1, N+2)]:
                is_passed = False
                break
            else:
                for j in range(i, i+L):
                    if board[row_num][j] != rear:
                        is_passed = False
                        break
                if is_passed:
                    is_possible_list[i+1: min(i+L+1, N+2)
                                     ] = [False] * (min(i+L+1, N+2) - (i+1))
                else:
                    break

    if is_passed:
        ans += 1
        # ans_list.append((row_num, -1))


# 세로 방향 체크
for col_num in range(N):
    is_possible_list = [False] + [True] * N + [False]
    is_passed = True
    for i in range(1, N):
        front = board[i-1][col_num]
        rear = board[i][col_num]
        if abs(front - rear) >= 2:
            is_passed = False
            break
        if rear - front == 1:  # 1 증가
            if False in is_possible_list[max(0, i+1-L): i+1]:
                is_passed = False
                break
            else:
                is_possible_list[max(0, i+1-L): i+1] = [False] * \
                    (i+1 - max(0, i+1-L))
        elif front - rear == 1:  # 1 감소
            if False in is_possible_list[i+1: min(i+L+1, N+2)]:
                is_passed = False
                break
            else:
                for j in range(i, i+L):
                    if board[j][col_num] != rear:
                        is_passed = False
                        break
                if is_passed:
                    is_possible_list[i+1: min(i+L+1, N+2)
                                     ] = [False] * (min(i+L+1, N+2) - (i+1))
                else:
                    break

    if is_passed:
        ans += 1
        # ans_list.append((-1, col_num))

print(ans)
# print(ans_list)
