import heapq as hq
def div_pow(n, i):
    cnt = 1
    while n % i == 0:
        n //= i
        cnt += 1
    return cnt

def num_div(e):
    result = [1] * (e + 1)
    result[1] = 1
    for i in range(2, e + 1):
        if result[i] > 1:
            continue
        for n in range(i, e + 1, i):
            result[n] *= div_pow(n, i)
    return result

def solution(e, starts):
    freq = num_div(e)
    sorted_starts = sorted(starts)
    mapping = {k: v for v, k in enumerate(starts)}
    s = sorted_starts[0]
    freq = [(-n, i) for i, n in enumerate(freq[s:])]
    hq.heapify(freq)
    sorted_starts = [n - s for n in sorted_starts]
    answer = [0] * len(starts)
    for n in sorted_starts:
        while freq[0][1] < n:
            hq.heappop(freq)
        answer[mapping[n + s]] = s + freq[0][1]
    return answer
