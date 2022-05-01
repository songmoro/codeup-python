a, b, c = map(int,input().split())
i = a if(a<b) else b
i = c if(c<i) else i

for i in range(i,a*b*c + 1):
    if (i % a == 0) and (i % b == 0) and (i % c == 0):
        print(i)
        break