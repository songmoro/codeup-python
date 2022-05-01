a = int(input())
i = 1
sum = 0
while 1:
    if a <= sum:
        print(i-1)
        break
    else:
       sum += i
       i += 1