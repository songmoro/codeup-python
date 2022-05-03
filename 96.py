d = [[int(x) for x in input().split()] for i in range(19)]

n = int(input())

for i in range(n):
    x, y = map(int,input().split())
    x -= 1
    y -= 1
    for j in range(19):
        d[x][j] = 1 if d[x][j] == 0 else 0
    for j in range(19):
        d[j][y] = 1 if d[j][y] == 0 else 0

for k in range(19):
    for j in range(19):
        print(d[k][j], end=' ')
    print()