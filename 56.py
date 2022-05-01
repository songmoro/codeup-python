a, b = map(int, input().split())
c = (bool(a) and not bool(b)) or (not bool(a) and bool(b))
print(c)