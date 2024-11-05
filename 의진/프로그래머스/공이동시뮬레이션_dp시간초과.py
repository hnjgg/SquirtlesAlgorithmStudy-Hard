from pprint import pprint

def get_dp(r, c, step, queries, dp, n, m):
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    
    if dp[r][c][step] != False:
        return dp[r][c][step]
    elif step == 0:
        dp[r][c][step] = {(r, c)}
        return dp[r][c][step]
    else:
        now_query = queries[step-1]

        if r == 0:
            if now_query[0] == 2:
                result = set()
                for i in range(now_query[1]+1):
                    if 0 <= r + i < n:
                        result = result.union(get_dp(r+i, c, step-1, queries, dp, n, m))
                dp[r][c][step] = result
                return dp[r][c][step]
        if r == n-1:
            if now_query[0] == 3:
                result = set()
                for i in range(now_query[1]+1):
                    if 0 <= r - i < n:
                        result = result.union(get_dp(r-i, c, step-1, queries, dp, n, m))
                dp[r][c][step] = result
                return dp[r][c][step]
        if c == 0:
            if now_query[0] == 0:
                result = set()
                for i in range(now_query[1]+1):
                    if 0 <= c + i < m:
                        result = result.union(get_dp(r, c+i, step-1, queries, dp, n, m))
                dp[r][c][step] = result
                return dp[r][c][step]
        if c == m-1:
            if now_query[0] == 1:
                result = set()
                for i in range(now_query[1]+1):
                    if 0 <= c - i < m:
                        result = result.union(get_dp(r, c-i, step-1, queries, dp, n, m))
                dp[r][c][step] = result
                return dp[r][c][step]
        
        pr = r - dr[now_query[0]] * now_query[1]
        pc = c - dc[now_query[0]] * now_query[1]
        if 0 <= pr < n and 0 <= pc < m:
            dp[r][c][step] = get_dp(pr, pc, step-1, queries, dp, n, m)
        else:
            dp[r][c][step] = set()
        return dp[r][c][step]            
            

def solution(n, m, x, y, queries):
    dp = [[[False for _ in range(len(queries)+1)] for _ in range(m)] for _ in range(n)]
    result = get_dp(x, y, len(queries), queries, dp, n, m)
    pprint(dp)
    return len(result)