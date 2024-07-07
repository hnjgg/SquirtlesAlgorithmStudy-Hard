def solution(words):
    ans = 0
    words = [""] + sorted(words) + [""]
    for i in range(1, len(words) - 1):
        j1 = j2 = 0
        lp = len(words[i - 1])
        l0 = len(words[i])
        ln = len(words[i + 1])
        while j1 < lp and j1 < l0 and words[i - 1][j1] == words[i][j1]:
            j1 += 1
        while j2 < l0 and j2 < ln and words[i][j2] == words[i + 1][j2]:
            j2 += 1
        j = max(j1, j2)
        if j < len(words[i]):
            j += 1
        ans += j

    return ans
