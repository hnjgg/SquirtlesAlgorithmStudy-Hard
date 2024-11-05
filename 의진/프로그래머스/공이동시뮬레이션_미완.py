def solution(n, m, x, y, queries):
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    s_r = x
    s_c = y
    e_r = x
    e_c = y

    is_stick_s_r = True if s_r == 0 else False
    is_stick_e_r = True if e_r == n-1 else False
    is_stick_s_c = True if s_c == 0 else False
    is_stick_e_c = True if e_c == m-1 else False
    
    for query in reversed(queries):
        if query[0] == 0: # 왼쪽
            if is_stick_s_c:
                e_c = min(e_c - dc[0] * query[1], m-1)
            elif is_stick_e_c:
                continue
            else:
                s_c = min(s_c - dc[0] * query[1], m-1)
                e_c = min(e_c - dc[0] * query[1], m-1)

            if e_c == m-1:
                is_stick_e_c = True
        
        if query[0] == 1: # 오른쪽
            if is_stick_e_c:
                s_c = max(s_c - dc[1] * query[1], 0)
            elif is_stick_s_c:
                continue
            else:
                s_c = max(s_c - dc[1] * query[1], 0)
                e_c = max(e_c - dc[1] * query[1], 0)

            if s_c == 0:
                is_stick_s_c = True

        if query[0] == 2: # 위로
            if is_stick_s_r:
                e_r = min(e_r - dr[2] * query[1], n-1)
            elif is_stick_e_r:
                continue
            else:
                s_r = min(s_r - dr[2] * query[1], n-1)
                e_r = min(e_r - dr[2] * query[1], n-1)

            if e_r == n-1:
                is_stick_e_r = True

        if query[0] == 3: # 아래로
            if is_stick_e_r:
                s_r = max(s_r - dr[3] * query[1], 0)
            elif is_stick_s_r:
                continue
            else:
                s_r = max(s_r - dr[3] * query[1], 0)
                e_r = max(e_r - dr[3] * query[1], 0)

            if s_r == 0:
                is_stick_s_r = True
        # print(query[0], s_r, s_c, e_r, e_c)


    answer = (e_r - s_r + 1) * (e_c - s_c + 1)
    return answer