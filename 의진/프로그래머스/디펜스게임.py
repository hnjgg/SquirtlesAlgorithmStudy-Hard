import heapq

def solution(n, k, enemy):
    total_enemy_num = 0
    answer = -1
    for i, e in enumerate(enemy):
        total_enemy_num += e
        if i < k-1:
            continue
        elif i == k-1:
            muzuk = enemy[:k]
            heapq.heapify(muzuk)
            muzuk_sum = sum(muzuk)
        else:
            if e > muzuk[0]:
                muzuk_sum = muzuk_sum - muzuk[0] + e
                heapq.heappop(muzuk)
                heapq.heappush(muzuk, e)
            
            if total_enemy_num - muzuk_sum > n:
                answer = i
                break
    
    if answer == -1:
        answer = len(enemy)
    return answer