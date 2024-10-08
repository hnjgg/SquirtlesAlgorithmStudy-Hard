def solution(e, starts):
    divisor = [1 for _ in range(e+1)]
    for mul in range(2, e+1):
        for i in range(mul, e+1, mul):
            divisor[i] += 1

    dp = [0 for _ in range(e+1)]
    dp[e] = (divisor[e], e)
    for i in range(e-1, min(starts)-1, -1):
        if divisor[dp[i+1]] <= divisor[i]:
            dp[i] = i
        else:
            dp[i] = dp[i+1]

    answer = []

    for s in starts:
        answer.append(dp[s])
    return answer