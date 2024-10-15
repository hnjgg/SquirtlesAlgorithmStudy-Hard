import sys

def is_matched(query, target):
    is_same = True
    is_inverted = True
    for q, t in zip(query, target):
        if q != t:
            is_same = False
    for q, t in zip(query, target):
        if int(q) != (1-int(t)):
            is_inverted = False
            
            
    # result = query ^ target
    # bit_length = max(len(bin(query)) - 2, len(bin(target)) - 2)
    
    if is_same:
        return 1
    elif is_inverted:
        return 2
    else:
        return 0
    
def flip_col_and_check_match(col_list, beginning, target):
    new_map = [[0] * len(beginning[0]) for _ in range(len(beginning))]
    for r in range(len(beginning)):
        for c in range(len(beginning[0])):
            if c in col_list:
                new_map[r][c] = 1-beginning[r][c]
            else:
                new_map[r][c] = beginning[r][c]

    change_row_num = 0
    for r, row in enumerate(new_map):
        row = "".join(map(str, row))
        t = "".join(map(str, target[r]))
        result = is_matched(row, t)
        if result == 0:
            return -1
        elif result == 2:
            change_row_num += 1
    
    return change_row_num + len(col_list)



def solution(beginning, target):
    cnt = 0
    answer = sys.maxsize
    list_of_col_lists = []
    for i in range(2**len(beginning[0])):
        current_col_list = []

        for bit in range(len(beginning[0])):
            if i & (1 << bit):
                current_col_list.append(bit)
        list_of_col_lists.append(current_col_list)
    

    for col_list in list_of_col_lists:
        result = flip_col_and_check_match(col_list, beginning, target)
        if not result == -1:
            answer = min(answer, result)
            cnt += 1

    if answer == sys.maxsize:
        answer = -1
        
    # print(cnt)
    return answer