import sys

def get_dp(r, c, dp, problems):
    if dp[r][c] != sys.maxsize:
        return dp[r][c]
    if r > 0:
        dp[r][c] = min(dp[r][c], get_dp(r-1, c, dp, problems) + 1)
        dp[r][c] = dp[r-1][c][1]
    if c > 0:
        dp[r][c] = min(dp[r][c], get_dp(r, c-1, dp, problems) + 1)
        dp[r][c] = dp[r][c-1][1]

    for prob in problems:
        if r-prob[2] >= prob[0] and c-prob[3] >= prob[1]:
            dp[r][c] = min(dp[r][c], get_dp(r-prob[2], c-prob[3], dp, problems) + prob[4])
    
    return dp[r][c]



def solution(alp, cop, problems):
    INF = sys.maxsize
    for prob in problems:
        prob[0] = max(0, prob[0] - alp)
        prob[1] = max(0, prob[1] - cop)

    
    alp_sorted_problems = sorted(problems, key=lambda x: -x[0])
    cop_sorted_problems = sorted(problems, key=lambda x: -x[1])
    max_alp = alp_sorted_problems[0][0]
    max_cop = cop_sorted_problems[0][1]

    dp = [[INF for _ in range(max_cop+1)] for _ in range(max_alp+1)]
    dp[0][0] = 0

    answer = get_dp(max_alp, max_cop, dp, problems)

    return answer