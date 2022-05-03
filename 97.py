h, w = map(int,input().split())
d = []

for i in range(h):
    d.append([])
    for j in range(w):
        d[i].append(int(0))

for i in range(int(input())):
    l, p, x, y = map(int,input().split())
    x -= 1
    y -= 1
    if p == 0:
        for j in range(l):
            d[x][y+j] = 1
    else:
        for j in range(l):
            d[x+j][y] = 1

for i in range(h):
    for j in range(w):
        print(d[i][j],end=' ')
    print()