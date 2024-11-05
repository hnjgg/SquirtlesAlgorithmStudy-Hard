import re
import copy

# Preprocess : O(U*B*len(U)), DFS : O(U^B) -> with Pruning -> O(uPb)
def solution(user_id, banned_id):
    match_info = [[] for _ in range(len(banned_id))]
    for i, b in enumerate(banned_id):
        b = b.replace("*", ".")
        b = re.compile(b)
        for u in user_id:
            if b.fullmatch(u):
                match_info[i].append(u)

    stack = []
    result_list = []
    sequence = []
    stack.append((sequence, 0))     

    while stack:
        sequence, idx = stack.pop()
        if idx == len(match_info):
            result_list.append(sequence)
        else:
            for m in match_info[idx]:
                if m not in sequence:
                    new_sequence = sequence + [m]
                    stack.append((new_sequence, idx + 1))
                
    result_set = set(map(tuple, map(sorted, result_list)))
    result_set = {item for item in result_set if len(set(item))== len(item)}
    answer = len(result_set)
    return answer