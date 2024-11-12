def solution(storey):
    deci = []
    while storey > 0:
        deci.append(storey % 10)
        storey //= 10
    s, e = 0, 1
    while deci:
        num = deci.pop()
        s, e = min(s + num, e + 10 - num), min(s + num + 1, e + 10 - num - 1)
    return s
