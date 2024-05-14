a,b,c,d=map(int,input().split())
s=0
if a*b+d<=a*c:
    print(a*b+d)
else:
    for i in range(a):
        if i*b+d<=i*c:
            print(s+a*b+d)
            exit()
        else:
            s+=c
            d-=(i*b-s)
    print(a*c)
