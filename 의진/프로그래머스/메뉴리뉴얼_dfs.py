from itertools import combinations
from collections import Counter
import copy

def dfs(node, new_char, new_char_i, test_set, course, info_dict, char_list, candidates):
    past_test_set = copy.copy(test_set)
    test_set = test_set.intersection(info_dict[new_char])
    if len(node) in course:
        if len(test_set) <= 1:
            test_set = past_test_set
            return candidates
        else:
            if candidates[len(node)][len(test_set)] != 0:
                candidates[len(node)][len(test_set)].append(node)
            else:
                candidates[len(node)][len(test_set)] = [node]

    if new_char_i + 1 < len(char_list):
        for offset, next_char in enumerate(char_list[new_char_i + 1:]):
            next_node = node + next_char
            next_i = new_char_i + 1 + offset
            candidates = dfs(next_node, next_char, next_i, test_set, course, info_dict, char_list, candidates)

    test_set = past_test_set
    return candidates


def solution(orders, course):
    candidates = [[0] * 20 for _ in range(20)]
    info_dict = {}
    char_list = []
    answer = []

    # info_dict = dict(Counter(orders))
    # print(info_dict)

    for i, o in enumerate(orders):
        for char in o:
            if info_dict.get(char) is None:
                info_dict[char] = set([i])
                char_list.append(char)
            else:
                info_dict[char].add(i)

    char_list.sort()
    for i, char in enumerate(char_list):
        candidates = dfs(char, char, i, info_dict[char], course, info_dict, char_list, candidates)

    for i in range(2, len(candidates)):
        for j in range(len(candidates[0])):
            if candidates[i][len(candidates[0]) - j - 1] != 0:
                answer += candidates[i][len(candidates[0]) - j - 1]
                break

    answer.sort()
    return answer