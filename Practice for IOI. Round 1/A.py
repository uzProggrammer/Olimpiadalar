f=lambda x:len(set(str(x)))
g=lambda x:f(x)**2*x
def s(l,r,m):
    s=0
    for x in range(l,r+1):s=(s+g(x))%m
    return s
for _ in range(int(input())):
    l,r,m=map(int, input().split())
    print(s(l,r,m))
