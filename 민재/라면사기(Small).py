n = int(input())
numbers = list(map(int, input().split()))


dp = [1000001 for i in range(n+3)]
dp[0] = 0
dp[1] = 0
dp[2] = 0
dp[3] = numbers[0] * 3

for i in range(4,len(numbers) + 3):
    idx = i - 3
    if numbers[idx] == 0:
        dp[i] = dp[i-1]
        continue
    two_case = dp[i-1-1] + 5
    three_case = dp[i-2-1] + 7
    one_case = dp[i-1] + numbers[idx] * 3
    print(two_case, three_case, one_case)
    min_res = 1000000
    min_res = min(
        two_case,
        three_case,
        one_case
    )
    dp[i] = min_res
    print(dp)
    if min_res == one_case:
        numbers[idx] = 0

    elif min_res == two_case:
        tmp = min(numbers[idx-1], numbers[idx])
        numbers[idx-1] -= tmp
        numbers[idx] -= tmp
    elif min_res == three_case:
        tmp = min(numbers[idx-2], numbers[idx-1], numbers[idx])
        numbers[idx-2] -= tmp
        numbers[idx-1] -= tmp
        numbers[idx] -= tmp
    
print(dp)
