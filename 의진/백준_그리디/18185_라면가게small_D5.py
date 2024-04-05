import sys
input = sys.stdin.readline

N = int(input())
factories = list(map(int, input().split())) + [0, 0]
result = 0

for i, factory in enumerate(factories[:-2]):
    if factories[i+1] > factories[i+2]:
        purchase = min(factories[i], factories[i+1]-factories[i+2])
        result += (5*purchase)
        factories[i] -= purchase
        factories[i+1] -= purchase

        purchase = min(factories[i], factories[i+1], factories[i+2])
        result += (7*purchase)
        factories[i] -= purchase
        factories[i+1] -= purchase
        factories[i+2] -= purchase

    else:
        purchase = min(factories[i], factories[i+1])
        result += (7*purchase)
        factories[i] -= purchase
        factories[i+1] -= purchase
        factories[i+2] -= purchase

    result += 3*factories[i]
    factories[i] = 0

print(result)
