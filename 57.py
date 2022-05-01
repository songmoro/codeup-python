a, b = map(int, input().split())
c = (bool(a) and bool(b)) or (not bool(a) and not bool(b))
print(c)