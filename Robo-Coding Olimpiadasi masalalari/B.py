n,m=map(int,input().split())
k=n//m
print(abs((n*(n+1)//2-m*k*(k+1)//2)-(m*k*(k+1)//2)))