import sys
input = sys.stdin.readline

sys.setrecursionlimit(100_000_000)


def get_answer(start_idx, end_idx):
    global histogram
    if len(histogram[start_idx:end_idx]) == 1:
        return histogram[start_idx]
    elif len(histogram[start_idx:end_idx]) == 0:
        return 0
    else:
        min_val = 1_000_000_001
        for offset, item in enumerate(histogram[start_idx:end_idx]):
            if item < min_val:
                divide_idx = offset + start_idx
                min_val = item

        answer = max(get_answer(start_idx, divide_idx),
                     get_answer(divide_idx+1, end_idx),
                     min_val * (end_idx - start_idx))
        return answer


while True:
    test_case = list(map(int, input().split()))
    if test_case[0] == 0:
        break
    histogram = test_case
    answer = get_answer(0, len(histogram))

    print(answer)
