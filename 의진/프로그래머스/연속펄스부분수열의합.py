def solution(sequence):
    new_seq = []
    current = 1
    for s in sequence:
        new_seq.append(s * current)
        current = -current

    dp_max = [0 for _ in range(len(sequence))]
    dp_min = [0 for _ in range(len(sequence))]
    
    dp_max[0] = new_seq[0]
    dp_min[0] = new_seq[0]

    for i in range(1, len(dp_max)):
        dp_max[i] = max(0, dp_max[i-1]) + new_seq[i]
        dp_min[i] = min(0, dp_min[i-1]) + new_seq[i]

    answer = max(abs(max(dp_max)), abs(min(dp_min[-1])))
    return answer