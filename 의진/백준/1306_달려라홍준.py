import sys
import heapq
import copy
input = sys.stdin.readline


def negative_int(x):
    return -int(x)


# Initialize
N, M = map(int, input().split())
ads = list(map(negative_int, input().split()))

window_start_idx = 0
window_end_idx = 2*M - 2

pq = copy.copy(ads)
pq = pq[:2*M - 1]
heapq.heapify(pq)

info_dict = {}
for ad in ads[window_start_idx: window_end_idx+1]:
    if info_dict.get(ad) is not None:
        info_dict[ad] += 1
    else:
        info_dict[ad] = 1

result = [-pq[0]]

# window 옮길 때마다 값 얻음
while window_end_idx < len(ads) - 1:
    # 1. 나가는 dict 변경 (만약 0 되면 아예 key 제거)
    exit_item = ads[window_start_idx]
    info_dict[exit_item] -= 1

    if info_dict[exit_item] == 0:
        del info_dict[exit_item]

    # 2. None인 heap 연달아 제거
    while True:
        if len(pq) == 0:
            break
        elif info_dict.get(pq[0]) is None:
            heapq.heappop(pq)
        else:
            break

    # 3. 들어온 dict 추가 -> 만약 신규 추가면 heap에 추가
    enter_item = ads[window_end_idx + 1]
    if info_dict.get(enter_item) is not None:
        info_dict[enter_item] += 1
    else:
        info_dict[enter_item] = 1
        heapq.heappush(pq, enter_item)

    # 4. 최댓값 추가
    result.append(-pq[0])

    # 5. idx 갱신
    window_start_idx += 1
    window_end_idx += 1

for item in result:
    print(item, end=" ")
