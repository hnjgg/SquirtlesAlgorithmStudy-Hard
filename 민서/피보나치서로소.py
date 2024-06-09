input = open(0).readline
def phi_func(n):
    phi = n
    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0:
            phi = phi - phi // k
            while n % k == 0:
                n = n // k
    if n > 1:
        phi = phi - phi // n
    return phi

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        if N <= 2:
            print(N - 1)
            continue
        phi = phi_func(N)
        if N % 4 == 0:
            phi += phi // 2
        elif N % 2 == 0:
            phi *= 2
        print(phi)

main()
