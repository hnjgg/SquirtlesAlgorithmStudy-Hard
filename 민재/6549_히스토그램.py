while True:
    heights = list(map(int, input().split()))
    if heights[0] == 0: break

    heights = heights[1:] + [0]
    stack = [(-1, -1)] # (idx, height)
    answer = 0
    for idx, h in enumerate(heights):
        while stack and stack[-1][1] > h:
            print(stack)
            prev_index, prev_height = stack.pop()
            width = idx - (stack[-1][0] + 1)
            area = width * prev_height
            answer = max(answer, area)
        
        stack.append((idx, h))

    print(answer)