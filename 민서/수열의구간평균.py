input = open(0).readline
N, K = map(int, input().split())
acc = [0] * (N+1)
dic = {}
i = 0
for n in input().split():
    acc[i+1] = acc[i] + int(n)
    i += 1
for i, n in enumerate(acc):
    n -= K * i
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1
ans = 0
for k, v in dic.items():
    ans += v * (v-1) // 2
print(ans)
