import math
a,b,h,m=map(int,input().split())
dh=(360//12)*h
dm=(360//60)*m
d=abs(dm-dh)
if d==180:
    print('%.5f'%float(a+b))
elif d==0:
    print('%.5f'%float(abs(a-b)))
elif d==90:
    print('%.5f'%((a**2+b**2)**0.5))
elif d<90:
    r=((a**2+b**2-2*a*b*math.cos(math.radians(d)))**0.5)
    print('%.5f'%r)
else:
    r=((a**2+b**2-2*a*b*math.cos(math.radians(d)))**0.5)
    print('%.5f'%r)