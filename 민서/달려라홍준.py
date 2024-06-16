import heapq as hq
input = open(0).readline
def main():
    N, M = map(int, input().split())
    arr = [(-n, i) for i, n in enumerate(map(int, input().split()))]
    k = 2 * M - 2
    pque = arr[:k]
    hq.heapify(pque)
    for i in range(k, N):
        hq.heappush(pque, arr[i])
        while pque[0][1] < i - k:
            hq.heappop(pque)
        print(-pque[0][0], end=" ")

main()
