a, b, c, d = map(int,input().split())
e = ((a * b * c * d) / 8) / (1024 ** 2)
print("%.1f"%e+" MB")