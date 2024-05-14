import math
a=int(input())
s=0
for i in range(1,a+1):
    s+=(i**2)/((2*i-1)*(2*i+1))
print(f'{s:.6f}')
print(a**2/((a+1)*3))