def solution(user_id, banned_id):
    new_list = []
    for id in banned_id:
        new_list.append([id,[]])
    
    for index, banned_id_ in enumerate(banned_id):
        for user_id_ in user_id:
            flag = 1
            for i in range(len(banned_id_)):
                if len(banned_id_) != len(user_id_):
                    flag = 0
                    break
                if banned_id_[i] == '*':
                    continue
                else:
                    if banned_id_[i] == user_id_[i]:
                        continue
                    else:
                        flag = 0
                        break
            if flag == 1:
                new_list[index][1].append(user_id_)
            else:
                continue
    path_list = []
    for element in new_list[0][1]:
        path_list.append([[element],0])
    
    total_path = []
    # dfs with pruning
    while path_list:
        # print(f'pathlist = {path_list}')
        temp_path = path_list.pop()
        if temp_path[1] == len(banned_id)-1:
            #print(f'update time path :\n{temp_path}')
            temp_path[0].sort()
            total_path.append(tuple(temp_path[0]))
            continue
        # print(f'new_list[temp_path[1]+1][1] = {new_list[temp_path[1]+1][1]}')
        for element in new_list[temp_path[1]+1][1]:
            if element not in temp_path[0]:
                append_list = temp_path[0][:]
                append_list.append(element)
                # print(f'temp_path[0][:] = {temp_path[0][:]}')
                # print(f'append_list = {append_list}')
                path_list.append([append_list,temp_path[1]+1])
    
    return len(set(total_path))