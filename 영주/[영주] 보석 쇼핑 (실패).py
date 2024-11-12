def solution(gems):
    answer = []
    gem_set_len = len(set(gems))
    gem_dict = {}

    start = 0
    end = 0
    sect = len(gems)+1

    while end < len(gems):
        if gems[end] not in gem_dict:
            gem_dict[gems[end]] = 1
        else:
            gem_dict[gems[end]] += 1

        end += 1

        if len(gem_dict) == gem_set_len:
            while start < end:
                if gem_dict[gems[start]] > 1:
                    gem_dict[gems[start]] -= 1
                    start += 1
                else:
                    break

    return answer
