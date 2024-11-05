def solution(a):
    stack = []
    for item in a:
        while True:
            if not stack:
                stack.append(item)
                break
            if stack[-1] > item:
                stack.pop()
            else:
                stack.append(item)
                break
    result = set(stack)

    stack = []
    for item in reversed(a):
        while True:
            if not stack:
                stack.append(item)
                break
            if stack[-1] > item:
                stack.pop()
            else:
                stack.append(item)
                break
    result = result.union(set(stack))
    
    return len(result)