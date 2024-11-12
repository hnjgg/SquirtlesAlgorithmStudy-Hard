import heapq

def solution(gems):
    candidates = []
    info_dict = {}
    key_len = 0
    num_of_kinds = len(set(gems))

    left = 0
    right = -1
    left_flag = False
    right_flag = False

    while not left_flag or not right_flag:
        while key_len != num_of_kinds and right < len(gems)-1:
            right += 1
            now = gems[right]
            if info_dict.get(now) is None:
                info_dict[now] = 1
                key_len += 1
            else:
                info_dict[now] += 1

        if right == len(gems)-1:
            right_flag = True

        while key_len == num_of_kinds:
            heapq.heappush(candidates, (right-left, left+1, right+1))
            left += 1
            prev = gems[left-1]
            info_dict[prev] -= 1
            if info_dict[prev] == 0:
                del info_dict[prev]
                key_len -= 1

        if right_flag:
            left_flag = True


    print(candidates)
    answer = [candidates[0][1], candidates[0][2]]
            
    return answer