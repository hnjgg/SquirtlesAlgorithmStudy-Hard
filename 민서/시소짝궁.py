from bisect import bisect_left, bisect_right

def bisect_count(a, x, lo):
    return bisect_right(a, x, lo) - bisect_left(a, x, lo)

def solution(weights):
    answer = 0
    weights = sorted(weights)
    for i, x in enumerate(weights):
        if x % 2 == 0:
            answer += bisect_count(weights, x // 2 * 3, i + 1)
        if x % 3 == 0:
            answer += bisect_count(weights, x // 3 * 4, i + 1)
        answer += bisect_count(weights, x, i + 1)
        answer += bisect_count(weights, x * 2, i + 1)
    return answer
