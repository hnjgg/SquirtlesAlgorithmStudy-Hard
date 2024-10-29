import re

# Preprocess : O(U*B*len(U)), DFS : O(U^B) with Pruning -> O(uPb)
def dfs(sequence, match_info, result_list):
    if len(sequence) == len(match_info):
        result_list.append(sequence)
        return sequence, result_list
    else:
        for m in match_info[len(sequence)]:
            if m not in sequence:
                sequence.append(m)
                sequence, result_list = dfs(sequence, match_info, result_list)
                sequence = sequence[:-1]
        return sequence, result_list


def solution(user_id, banned_id):
    match_info = [[] for _ in range(len(banned_id))]
    for i, b in enumerate(banned_id):
        b = b.replace("*", ".")
        b = re.compile(b)
        for u in user_id:
            if b.fullmatch(u):
                match_info[i].append(u)
    _, result_list = dfs([], match_info, [])
    result_set = set(map(tuple, map(sorted, result_list)))
    result_set = {item for item in result_set if len(set(item))== len(item)}
    answer = len(result_set)
    return answer