import sys
input = sys.stdin.readline

n = int(input())
tree = [0]*(4*10**6)  # 세그먼트 트리


def putCandy(left, right, node, b, c):
    # b => 사탕 맛, c => 사탕 개수
    tree[node] += c
    if left == right:
        return
    mid = (left+right) // 2
    if b <= mid:
        # 맛이 왼쪽 구간에 포함된 경우
        putCandy(left, mid, node*2, b, c)
    else:
        # 맛이 오른쪽 구간에 포함된 경우
        putCandy(mid+1, right, node*2+1, b, c)


def findCandy(left, right, node, b):
    # b => 순위
    tree[node] -= 1
    if left == right:
        # 리프노드
        return left  # 빼내는 사탕의 맛
    mid = (left+right) // 2
    if tree[node*2] >= b:
        # 원하는 사탕이 왼쪽 구간에 있음
        return findCandy(left, mid, node*2, b)
    else:
        # 왼쪽 구간의 사탕 개수만큼 순위에서 제거
        return findCandy(mid+1, right, node*2+1, b-tree[node*2])


for _ in range(n):
    line = list(map(int, input().rstrip().split()))
    if len(line) == 2:
        b = line[1]
        print(findCandy(1, 10**6, 1, b))
    elif len(line) == 3:
        _, b, c = line
        putCandy(1, 10**6, 1, b, c)
