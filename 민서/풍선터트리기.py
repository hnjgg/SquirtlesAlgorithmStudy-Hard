def solution(a):
    ans = [False] * len(a)
    mn = 1<<30
    for i in range(len(a)):
        if a[i] < mn:
            ans[i] = True
            mn = a[i]
    mn = 1<<30
    for i in range(len(a) - 1, -1, -1):
        if a[i] < mn:
            ans[i] = True
            mn = a[i]
    return sum(ans)
