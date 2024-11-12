def solution(gems):
    max_kinds = len(set(gems))
    dic = {}
    l, r = 0, 0
    n_kinds = 0
    while n_kinds < max_kinds:
        g = gems[r]
        if dic.get(g) is not None:
            dic[g] += 1
        else:
            dic[g] = 1
            n_kinds += 1
        r += 1
    answer = [l + 1, r]
    mn = r - l
    while r < len(gems):
        while n_kinds == max_kinds:
            g = gems[l]
            dic[g] -= 1
            if dic[g] == 0:
                need = g
                n_kinds -= 1
            l += 1
        if r - l < mn:
            mn = r - l
            answer = [l, r]
        while r < len(gems) and n_kinds < max_kinds:
            g = gems[r]
            if g == need:
                n_kinds += 1
            dic[g] += 1
            r += 1
    while n_kinds == max_kinds:
        g = gems[l]
        dic[g] -= 1
        if dic[g] == 0:
            need = g
            n_kinds -= 1
        l += 1
    if r - l < mn:
        mn = r - l
        answer = [l, r]
    return answer
