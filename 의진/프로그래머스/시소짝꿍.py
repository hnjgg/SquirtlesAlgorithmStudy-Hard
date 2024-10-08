import itertools
def solution(weights):
    count_dict = {}
    info_dict = {}
    answer = 0

    for w in weights:
        if count_dict.get(w) is None:
            count_dict[w] = 1
        else:
            count_dict[w] += 1

    for k, v in count_dict.items():
        if v >= 2:
            answer += (v * (v-1) // 2)

    for w in set(weights):
        for mul in [2, 3, 4]:
            if info_dict.get(mul * w) is None:
                info_dict[mul*w] = [count_dict[w]]
            else:
                info_dict[mul*w].append(count_dict[w])
    for k, v in info_dict.items():
        if len(v) >= 2:
            comb = itertools.combinations(v, 2)
            for c in comb:
                answer += (c[0] * c[1])
    
    return answer