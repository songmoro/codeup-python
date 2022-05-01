a, b, c = map(int,input().split())
e = ((a * b * c) / 8) / (1024 ** 2)
print("%.2f"%e+" MB")