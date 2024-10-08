def solution(e, starts):
    divisor = [0]*(e+1)
    for i in range(1, e + 1):
        if i * i <= e:
            divisor[i*i] += 1
        for j in range(i+1, e + 1):
            n = i * j
            if n > e:
                break
            divisor[n] += 2

    dp = [0 for _ in range(e+1)]
    dp[e] = (divisor[e], e)
    for i in range(e-1, min(starts)-1, -1):
        if dp[i+1][0] <= divisor[i]:
            dp[i] = (divisor[i], i)
        else:
            dp[i] = dp[i+1]

    answer = []

    for s in starts:
        answer.append(dp[s][1])
    return answer