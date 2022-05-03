n = int(input())
d = input().split()
min = int(d[0])

for i in range(0,n):
    if min > int(d[i]):
        min = int(d[i])

print(min)