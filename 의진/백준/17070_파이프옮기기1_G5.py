import sys
input = sys.stdin.readline

N = int(input())
board = [[0] * (N + 1)] + [[0] + list(map(int, input().split()))
                           for _ in range(N)]

dp = [[[-1 for _ in range(3)] for _ in range(N+1)] for _ in range(N+1)]


for i in range(3):
    dp[1][1][i] = 0
    dp[1][2][i] = 0
    dp[2][1][i] = 0
    dp[2][2][i] = 0

dp[1][2][0] = 1


def get_dp(r, c, shape):
    if not ((0 < r <= N) and (0 < c <= N)):
        return 0
    elif dp[r][c][shape] != -1:
        return dp[r][c][shape]

    else:
        if board[r][c] == 0:
            if shape == 0:
                dp[r][c][shape] = (get_dp(r, c-1, 0) + get_dp(r, c-1, 1))
            elif shape == 2:
                dp[r][c][shape] = (get_dp(r-1, c, 1) + get_dp(r-1, c, 2))

            else:
                if board[r-1][c] == 0 and board[r][c-1] == 0:
                    dp[r][c][shape] = (get_dp(r-1, c-1, 0) +
                                       get_dp(r-1, c-1, 1) + get_dp(r-1, c-1, 2))
                else:
                    dp[r][c][shape] = 0
        else:
            dp[r][c][shape] = 0

    return dp[r][c][shape]


print(get_dp(N, N, 0) + get_dp(N, N, 1) + get_dp(N, N, 2))
