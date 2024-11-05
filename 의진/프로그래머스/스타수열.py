from bisect import bisect_left

def get_max_length(seq):
    if len(seq) == 1:
        return 1
    elif len(seq) == 2:
        if seq[0] + 1 == seq[1]:
            return 1
        else:
            return 2
        
    result = 0

    increasing_list = [seq[0]]
    for s in seq[1:]:
        if s-1 == increasing_list[-1]:
            continue
        else:
            increasing_list.append(s)

    result = len(increasing_list)

    # increasing_list = [seq[1]]
    # for s in seq[2:]:
    #     if s-1 == increasing_list[-1]:
    #         continue
    #     else:
    #         increasing_list.append(s)
    # result = max(result, len(increasing_list))

    return result
    

def solution(a):
    if len(a) == 1:
        return 0

    info_dict = {}

    for i in range(len(a)-1):
        if info_dict.get(a[i]) is None:
            info_dict[a[i]] = [i]
        else:
            info_dict[a[i]].append(i)

        if info_dict.get(a[i+1]) is None:
            info_dict[a[i+1]] = [i]
        else:
            if info_dict[a[i+1]][-1] != i:
                info_dict[a[i+1]].append(i)
            else:
                info_dict[a[i+1]].pop()
    
    answer = 0
    for k, v in info_dict.items():
        answer = max(answer, get_max_length(v))

        
    return answer * 2