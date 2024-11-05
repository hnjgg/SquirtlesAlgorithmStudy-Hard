from collections import Counter

a = [1, 3, 2, 3, 4, 3, 5]
b = [1, 3, 2, 3]

cnt_dict = Counter(a) - Counter(b)
print(cnt_dict)
# cnt_dict = {}
# for item in a:
#     if cnt_dict.get(item) is None:
#         cnt_dict[item] = 1
#     else:
#         cnt_dict[item] += 1