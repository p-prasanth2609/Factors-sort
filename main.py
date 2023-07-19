a = list(map(int, input().split()))
b=[]
for i in range(len(a)):
    count=0
    for j in range(1, a[i] + 1):
        if a[i] % j == 0:
            count+=1
    b.append(count)
d=zip(b,a)
d=[y for z,y in sorted(d)]
print(d)


