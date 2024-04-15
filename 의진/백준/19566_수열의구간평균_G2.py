import sys
import math

input = sys.stdin.readline

N, K = map(int, input().split())


def minus_k(item):
    return int(item) - K


seq = list(map(minus_k, input().split()))

prefix_sum = [0]
accumulate = 0

for element in seq:
    accumulate += element
    prefix_sum.append(accumulate)

info_dict = {}

for element in prefix_sum:
    if info_dict.get(element) is None:
        info_dict[element] = 1
    else:
        info_dict[element] += 1

result = 0
for value in info_dict.values():
    if value >= 2:
        result += math.comb(value, 2)
print(result)
