import sys

def solution(scores):
    # Naming
    named_scores = []
    for i, s in enumerate(scores):
        if i == 0:
            named_scores.append(s + [1])
        else:
            named_scores.append(s + [0])
    
    # Named Score Sorting
    named_scores.sort(key=lambda x: (-x[0], -x[1], -x[2]))

    # Get Candidates
    candidates = []
    current_thres_score = -1
    current_score_a = named_scores[0][0]
    measuring_thres_score = -1

    for ns in named_scores:
        if ns[0] != current_score_a:
            current_thres_score = max(measuring_thres_score, current_thres_score)
            measuring_thres_score = -1
            current_score_a = ns[0]

        measuring_thres_score = max(measuring_thres_score, ns[1])
        if ns[1] >= current_thres_score:
            candidates.append((ns[0] + ns[1], ns[2]))

    # print(candidates)
    # Candidates Sorting
    candidates.sort(key=lambda x: (-x[0], -x[1]))

    answer = -1
    for i in range(len(candidates)):
        if candidates[i][1] == 1:
            answer = i + 1
            break

    return answer


x = {i:int(input()) for i in range(10)}