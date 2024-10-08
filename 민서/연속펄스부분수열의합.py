def solution(sequence):
    end = len(sequence)
    if end == 1:
        return abs(sequence[0])
    for i in range(1, end, 2):
        sequence[i] = -sequence[i]
    cumsum = [0]
    for num in sequence:
        cumsum.append(cumsum[-1] + num)
    return max(cumsum) - min(cumsum)
