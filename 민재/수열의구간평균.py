from collections import defaultdict

n, k = map(int, input().split())
nums = list(map(int, input().split()))


change = [0 for i in range(n)]
res_dict = defaultdict(int)
res_dict[0] = 1
prefix = 0
answer = 0
for i in range(n):
    change[i] = nums[i] - k
    prefix += change[i]
    
    if prefix in res_dict:
        answer += res_dict[prefix]
    
    res_dict[prefix] += 1

print(res_dict)
print(answer)
