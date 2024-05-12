import sys
import heapq

input = sys.stdin.readline

T = int(input())

def set_to_sorting(item):
    return (item[1], item[0])

for _ in range(T):
    N, M = map(int, input().split())
    ab_list = [list(map(int, input().split())) for _ in range(M)]
    is_booked = [False for _ in range(N + 1)]
    result = 0
    
    ab_list = list(map(set_to_sorting, ab_list))

    heapq.heapify(ab_list)

    first_item = heapq.heappop(ab_list)
    current_b = first_item[0]
    is_next_item = True
    
    while ab_list or is_next_item:
        item_list = []
        is_next_item = False
        next_item = None
        while True:
            if not ab_list:
                break
            item = heapq.heappop(ab_list)
            if item[0] > current_b:
                next_item = item
                is_next_item = True
                current_b = item[0]
                break
            item_list.append(item)

        item_list = [first_item] + item_list
        if next_item is not None:
            first_item = next_item

        for item in item_list:
            for i in range(item[1], item[0] + 1):
                if not is_booked[i]:
                    result += 1
                    is_booked[i] = True
                    is_success = True
                    break
    print(result)