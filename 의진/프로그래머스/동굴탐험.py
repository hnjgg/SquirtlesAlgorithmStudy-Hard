from collections import deque
import sys
sys.setrecursionlimit(100_000_000)


def make_directed(parent, directed_path, bi_directed_path, visited, indegrees):
    visited[parent] = True
    for child in bi_directed_path[parent]:
        if visited[child] == False:
            directed_path[parent].append(child)
            indegrees[child] += 1
            make_directed(child, directed_path, bi_directed_path,
                          visited, indegrees)


def solution(n, path, order):
    bi_directed_path = [[] for _ in range(n)]
    directed_path = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    indegrees = [0 for _ in range(n)]
    queue = deque()

    for item in path:
        bi_directed_path[item[0]].append(item[1])
        bi_directed_path[item[1]].append(item[0])

    make_directed(0, directed_path, bi_directed_path, visited, indegrees)

    for item in order:
        directed_path[item[0]].append(item[1])
        indegrees[item[1]] += 1

    # print(num_entry_points)
    # 여기서부터 directed_path는 수정되면 안됨

    for idx, indegree in enumerate(indegrees):
        if indegree == 0:
            queue.append(idx)

    for _ in range(n):
        if len(queue) == 0:
            return False

        idx = queue.popleft()
        for next_node in directed_path[idx]:
            indegrees[next_node] -= 1
            if indegrees[next_node] == 0:
                queue.append(next_node)
    return True


print(solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6],
      [1, 2], [4, 7], [7, 5]], [[4, 1], [8, 7], [6, 5]]))
