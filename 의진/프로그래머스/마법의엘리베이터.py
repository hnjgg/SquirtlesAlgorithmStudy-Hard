def solution(storey):
    answer = 0
    storey = [0] + list(map(int, list(str(storey))))
    for i, s in enumerate(storey):
        if s < 5:
            answer += s
            storey[i] = 0
    for i, s in enumerate(reversed(storey)):
        i = len(storey) - i - 1
        if s != 0:
            if i != 0:
                if s >= 5:
                    storey[i-1] += 1
                    answer += (10 - s)
                else:
                    answer += 1
            else:
                answer += 1


    return answer