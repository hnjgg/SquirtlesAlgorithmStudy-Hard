input = open(0).readline
INF = 1<<30
def main():
    N, K = map(int, input().split())
    if N == K:
        print(0)
        return
    memo = [[INF] * 500001, [INF] * 500001]
    que = [N]
    memo[0][N] = 0
    i = 1
    while K + i <= 500000:
        K += i
        nque = []
        for n in que:
            for nn in [n * 2, n - 1, n + 1]:
                if 0 <= nn <= 500000:
                    if memo[i % 2][nn] > i:
                        memo[i % 2][nn] = i
                        nque.append(nn)
        que = nque
        if memo[i % 2][K] <= i:
            print(i)
            return
        i += 1
    print(-1)
    return
main()
