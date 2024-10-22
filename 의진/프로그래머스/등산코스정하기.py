import copy
INF = int(1e9)


def solution(n, paths, gates, summits):
    path_dict = {i: [] for i in range(1, n+1)}
    for path in paths:
        path_dict[path[0]].append((path[1], path[2]))
        path_dict[path[1]].append((path[0], path[2]))

    result = (0, INF)
    for gate in gates:
        explore_result = explore(n, summits, gates, path_dict, gate)
        if explore_result[1] < result[1]:
            result = explore_result

    answer = list(result)
    return answer


def get_smallest_node(n, dp, visited):
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if dp[i] < min_value and not visited[i]:
            min_value = dp[i]
            index = i
    return index


def explore(n, summits, gates, path_dict, gate):
    dp = {node: INF for node in range(1, n+1)}
    local_path_dict = copy.deepcopy(path_dict)
    visited = [False] * (n+1)
    dp[gate] = INF
    visited[gate] = True
    for item in gates:
        if item in gates and item != gate:
            local_path_dict[item] = []

    for item in local_path_dict[gate]:
        dp[item[0]] = item[1]

    for i in range(n-(len(gates)-1)):
        now = get_smallest_node(n, dp, visited)
        visited[now] = True

        for j in local_path_dict[now]:
            dp[j[0]] = min(dp[j[0]], dp[now], j[1])

    result_summit = 0
    result_intensity = INF
    for summit in summits:
        if dp[summit] < result_intensity:
            result_intensity = dp[summit]
            result_summit = summit
        elif dp[summit] == result_intensity:
            result_summit = min(summit, result_summit)
    return result_summit, result_intensity
