def solution(n, m, x, y, queries):
    x1 = x4 = x
    y1 = y4 = y
    for way, d in reversed(queries):
        if way == 0:
            if y1 == 0:
                continue
            y1 += d
        elif way == 1:
            y1 -= d
        elif way == 2:
            if x1 == 0:
                continue
            x1 += d
        elif way == 3:
            x1 -= d
        if x1 < 0:
            x1 = 0
        if x1 > n - 1:
            x1 = n - 1
        if y1 < 0:
            y1 = 0
        if y1 > m - 1:
            y1 = m - 1

    for way, d in reversed(queries):
        if way == 0:
            y4 += d
        elif way == 1:
            if y4 == m - 1:
                continue
            y4 -= d
        elif way == 2:
            x4 += d
        elif way == 3:
            if x4 == n - 1:
                continue
            x4 -= d
        if x4 < 0:
            x4 = 0
        if x4 > n - 1:
            x4 = n - 1
        if y4 < 0:
            y4 = 0
        if y4 > m - 1:
            y4 = m - 1

    answer = (x4 - x1 + 1) * (y4 - y1 + 1)
    return answer
