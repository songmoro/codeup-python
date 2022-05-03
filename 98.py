d = [[int(x) for x in input().split()] for i in range(10)]
n = 12
x = 1
y = 1

while n:
    if d[x][y] == 0:
        d[x][y] = 9
    elif d[x][y] == 2:
        d[x][y] = 9
        break
    if d[x][y+1] != 1:
        y += 1
    elif d[x][y+1] == 1 and d[x+1][y] != 1:
        x += 1
    else:
        break

for i in range(10):
    for j in range(10):
        print(d[i][j],end=' ')
    print()