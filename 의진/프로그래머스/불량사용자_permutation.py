import re
from itertools import permutations

# O((uPb) * B * len(U))
def solution(user_id, banned_id):
    answer = 0

    banned_id = [i.replace("*", ".") for i in banned_id]

    result = set()
    for i in permutations(user_id, len(banned_id)):
        i = list(i)
        check = True
        for j in range(len(i)):
            if re.fullmatch(banned_id[j], i[j]):
                continue
            else:
                check = False
                break

        if check:
            result.add(tuple(sorted(i)))

    answer = len(result)
    return answer
