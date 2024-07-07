input = open(0).readline

def EEA(a, b):
    s0, t0 = 1, 0
    s1, t1 = 0, 1
    while b:
        q = a // b
        a, b = b, a - b * q
        s0, s1 = s1, s0 - s1 * q
        t0, t1 = t1, t0 - t1 * q
    return a, s0, t0

def testcase(K, C):
    r, s, t = EEA(K, C)
    if r != 1:
        print("IMPOSSIBLE")
        return
    ans = t + K if s >= 0 else t
    if ans > 1000000000:
        print("IMPOSSIBLE")
        return
    print(ans)

def main():
    t = int(input())
    for _ in range(t):
        K, C = map(int, input().split())
        testcase(K, C)

main()
