import sys
from math import ceil, log
sys.setrecursionlimit(1 << 20)
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
INF = 1 << 31
ans = 0


class SegTreeForMin:
    def __init__(self, nums):
        self.nums = nums
        self.height = ceil(log(len(nums), 2))
        self.size = (1 << (self.height + 1)) - 1
        self.tree = [0] + [0] * self.size
        self._value_init(1, 0, len(self.nums)-1)

    def _value_init(self, node, start, end):
        if start == end:
            self.tree[node] = (self.nums[start], start)
            return self.tree[node]
        mid = (start + end) // 2
        # print(start, end, node)
        left = self._value_init(node*2, start, mid)
        right = self._value_init(node*2+1, mid+1, end)
        if left[0] <= right[0]:
            self.tree[node] = left
        else:
            self.tree[node] = right

        return self.tree[node]

    def _query_min_idx(self, start, end, q_start, q_end, node):
        if q_start == q_end:
            return (self.nums[q_start], q_start)
        if q_start > end or q_end < start:
            return (INF, -1)
        if q_start <= start and q_end >= end:
            return self.tree[node]
        mid = (start+end) // 2
        left = self._query_min_idx(start, mid, q_start, q_end, node * 2)
        right = self._query_min_idx(mid+1, end, q_start, q_end, node * 2 + 1)
        if left[0] <= right[0]:
            return left
        else:
            return right

    def query_min_idx(self, q_start, q_end):
        return self._query_min_idx(0, len(self.nums)-1, q_start, q_end, 1)


def get_prefix_sum(query):
    prefix_sum = [0]
    prev_sum = 0
    for idx, element in enumerate(query):
        prev_sum += element
        prefix_sum.append(prev_sum)

    return prefix_sum


def solve(start, end):
    if start > end:
        return
    global ans
    min_val, min_idx = seg_tree.query_min_idx(start, end)
    if min_idx == -1:
        return
    candidate = (prefix_sum[end+1] - prefix_sum[start]) * min_val
    ans = max(ans, candidate)

    solve(start, min_idx-1)
    solve(min_idx+1, end)


seg_tree = SegTreeForMin(A)
prefix_sum = get_prefix_sum(A)

solve(0, len(A)-1)

print(ans)
