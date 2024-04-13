# https://www.acmicpc.net/source/38784402
# https://www.acmicpc.net/source/76914640
input = open(0).readline

solution(arr):
    now2 = now3 = prev1 = prev2 = cost = 0
    for now1 in arr:
        now2 = min(now1, prev1)
        now1 -= now2
        now3 = min(now1, prev2)
        now1 -= now3
        cost += now1 * 3 + now2 * 2 + now3 * 2
        prev1, prev2 = now1, now2
    return cost

if __name__ == "__main__":
    input()
    arr = [*map(int, input().split())]
    print(solution(arr))
    # print(solution([1, 0, 1]))
    # print(solution([1, 1, 1, 0, 2])
